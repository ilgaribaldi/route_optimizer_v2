from utils import matrix
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math


# on demand request verification
def verify_rec(req):
    n_locations = len(req['clients'])
    rsp = 1

    if req['api'] != 'google' and req['api'] != 'billions':
        rsp = {'status': "INVALID REQUEST: invalid API"}

    if req['api'] == 'google' and n_locations > 25:
        rsp = {'status': "INVALID REQUEST: too many packages for google API, use billions API instead"}

    return rsp


# on demand request setup
def format_rec(request):
    f_r = {'lat': [], 'lng': [], 'address': [], 'contact': [], 'client_id': []}

    # Depot data
    f_r['lat'].append(request['lat'])
    f_r['lng'].append(request['lng'])
    f_r['address'].append(request['address'])
    f_r['contact'].append(request['contact'])

    # Clients data
    for client in request['clients']:
        f_r['lat'].append(client['lat'])
        f_r['lng'].append(client['lng'])
        f_r['address'].append(client['address'])
        f_r['contact'].append(client['contact'])
        f_r['client_id'].append(client['id'])

    # Additional data
    f_r['n_locations'] = len(request['clients'])
    f_r['api'] = request['api']

    # Defining search strategies
    if f_r['n_locations'] <= 25:  # 10 seconds
        f_r['time'] = 3
        f_r['search_strategies'] = 3
    elif f_r['n_locations'] <= 50:  # 15 seconds
        f_r['time'] = 3
        f_r['search_strategies'] = 3

    # Defining location demands
    f_r['demands'] = [0] + [1] * f_r['n_locations'] + [0]

    # obtaining cost matrix
    if request['api'] == 'google':
        f_r['cost_matrix'] = matrix.google(request)
    elif request['api'] == 'billions':
        f_r['cost_matrix'] = matrix.billions(request)
    return f_r


# solve on demand request
def solve_rec(f_req):
    # Define max time per route
    if f_req['api'] == 'google':
        max_time = 3000
    else:
        max_time = 2500

    # Define cost matrix
    C = f_req['cost_matrix']

    # Define initial attempt and vehicle number
    attempt = 0
    vehicles = math.ceil(f_req['n_locations'] / 20)

    # Create lists to store solution
    final_times = []
    final_routes = []

    while not final_times and attempt < 12:
        if attempt == 0:
            pass
        else:
            vehicles += 1

        attempt += 1
        capacities = [20] * vehicles
        starts = [len(f_req['lat'])] * vehicles
        ends = [0] * vehicles

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(C),
                                               vehicles,
                                               starts,
                                               ends)

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)

        # Create and register a transit callback.
        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return C[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Add Distance constraint.
        dimension_name = 'Distance'
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            max_time,  # vehicle maximum travel time
            True,  # start cumulative to zero
            dimension_name)
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(100)

        # Add Capacity constraint.
        def demand_callback(from_index):
            """Returns the demand of the node."""
            # Convert from routing variable Index to demand NodeIndex.
            from_node = manager.IndexToNode(from_index)
            return f_req['demands'][from_node]

        demand_callback_index = routing.RegisterUnaryTransitCallback(
            demand_callback)
        routing.AddDimensionWithVehicleCapacity(
            demand_callback_index,
            0,  # null capacity slack
            capacities,  # vehicle maximum capacities
            True,  # start cumulative to zero
            'Capacity')

        # set up routes & times lists to contain data for each search-strategy
        routes = []
        times = []
        rt_times = []

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()

        for trial in range(f_req['search_strategies']):
            if trial == 0:
                search_parameters.first_solution_strategy = (
                    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)
            elif trial == 1:
                search_parameters.first_solution_strategy = (
                    routing_enums_pb2.FirstSolutionStrategy.GLOBAL_CHEAPEST_ARC)
            elif trial == 2:
                search_parameters.first_solution_strategy = (
                    routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION)
            elif trial == 3:
                search_parameters.first_solution_strategy = (
                    routing_enums_pb2.FirstSolutionStrategy.SAVINGS)
            elif trial == 4:
                search_parameters.first_solution_strategy = (
                    routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC)

            if f_req['time'] == 0:  # If condition is satisfied, return optimal solution as fast as possible
                search_parameters.local_search_metaheuristic = (
                    routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC)
            else:  # If condition is not satisfied, return solution as fast as possible or when time runs out
                search_parameters.local_search_metaheuristic = (
                    routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)  # GUIDED_LOCAL_SEARCH
                search_parameters.time_limit.FromSeconds(f_req['time'])

            # Solve the problem.
            sol = routing.SolveWithParameters(search_parameters)

            # Generate route arrays
            rts = [None] * vehicles
            rts = np.array(rts)
            if sol:
                for vehicle_id in range(manager.GetNumberOfVehicles()):
                    rts[vehicle_id] = 0
                    previous_index = routing.Start(vehicle_id)
                    while not routing.IsEnd(previous_index):
                        index = sol.Value(routing.NextVar(previous_index))
                        end_node = manager.IndexToNode(index)
                        rts[vehicle_id] = np.append(rts[vehicle_id], end_node)
                        previous_index = index

                    # Deleting dummy nodes
                    rts[vehicle_id] = np.delete(rts[vehicle_id], 0)

            # Calculate route times and total time
            total_time = 0  # Initializing total distance
            route_times = []
            for route_number, route in enumerate(rts):
                route_time = 0
                if route is not None and len(route) > 1:
                    for idx in range(len(route) - 1):
                        route_time += f_req['cost_matrix'][route[idx]][route[idx + 1]]
                    route_times.append(route_time)
                    total_time += route_time
                else:
                    break

            routes.append(rts)
            times.append(total_time)
            rt_times.append(route_times)

        min_value = min(times)
        index = times.index(min_value)
        final_routes = routes[index]
        final_times = rt_times[index]

    if final_times:
        return final_routes
    else:
        return None


# get on demand response
def get_rec_response(f_req, sol):
    if sol is not None:
        rsp = {'status': 'OK', 'routes': []}  # Creating response dictionary
        for route_number, route in enumerate(sol):
            rt = []
            if len(route) > 1:
                for idx, node in enumerate(route):
                    picks = []
                    drops = []
                    address = f_req['address'][node]
                    contact = f_req['contact'][node]
                    if idx == 0:
                        time = 0
                    else:
                        seconds = f_req['cost_matrix'][route[idx-1]][route[idx]]
                        time = round(seconds / 60, 2)
                    if node == 0 and idx != len(route) - 1:  # if satisfied, node represents client
                        for other_node in route:
                            if other_node > 0:
                                picks.append(f_req['client_id'][other_node - 1])
                    elif node == 0 and idx == len(route) - 1:  # if satisfied, node represents client endpoint
                        pass
                    else:
                        drops.append(f_req['client_id'][node - 1])
                    node_info = {'address': address,
                                 'contact': contact,
                                 'picks': [],
                                 'drops': [],
                                 'time until stop': f'{time} min'}
                    rt.append(node_info)
                rsp['routes'].append(rt)
    else:
        rsp = {'status': "Error: No solution found for all routes under 30 minutes"}
    return rsp
