from utils import matrix
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


# main depot request verification
def verify_md(req):
    n_deliveries = len(req['parcels'])
    parcel_id = []
    for parcel in req['parcels']:
        parcel_id.append(parcel['id'])
    rsp = 1

    # Check if total vehicle capacity is enough for all parcels
    if req['capacities'] * req['vehicles'] < n_deliveries:
        rsp = {'status': 'INVALID REQUEST: not enough vehicles for packages'}

    # Check if depot_return > vehicle number
    if len(req['end_locations']) > req['vehicles']:
        rsp = {'status': 'INVALID REQUEST: too many end locations'}

    if n_deliveries > 150:
        rsp = {'status': "INVALID REQUEST: too many packages for optimizer"}

    if req['vehicles'] > n_deliveries:
        rsp = {'status': "INVALID REQUEST: too many vehicles"}

    for end_location in req['end_locations']:
        if end_location != 'depot' and end_location not in parcel_id:
            rsp = {'status': "INVALID REQUEST: invalid end location"}
            break
    return rsp


# main depot request setup
def format_md(request):
    f_r = {'lat': [], 'lng': [], 'address': [], 'contact': [], 'parcel_id': []}

    # Client data
    f_r['lat'].append(request['lat'])
    f_r['lng'].append(request['lng'])
    f_r['address'].append(request['address'])
    f_r['contact'].append(request['contact'])

    # Parcel data
    for parcel in request['parcels']:
        f_r['lat'].append(parcel['lat'])
        f_r['lng'].append(parcel['lng'])
        f_r['address'].append(parcel['address'])
        f_r['contact'].append(parcel['contact'])
        f_r['parcel_id'].append(parcel['id'])

    # Additional data
    f_r['n_deliveries'] = len(request['parcels'])
    f_r['vehicles'] = request['vehicles']

    if f_r['n_deliveries'] <= 25:  # 10 seconds
        f_r['time'] = 3
        f_r['search_strategies'] = 5
    elif f_r['n_deliveries'] <= 50:  # 15 seconds
        f_r['time'] = 3
        f_r['search_strategies'] = 5
    elif f_r['n_deliveries'] <= 75:  # 20 seconds
        f_r['time'] = 4
        f_r['search_strategies'] = 5
    elif f_r['n_deliveries'] <= 100:  # 25 seconds
        f_r['time'] = 6
        f_r['search_strategies'] = 4
    elif f_r['n_deliveries'] <= 150:  # 27 seconds
        f_r['time'] = 9
        f_r['search_strategies'] = 3

    # Defining location demands and capacities
    f_r['demands'] = [0] + [1] * f_r['n_deliveries'] + [0]
    f_r['capacities'] = [request['capacities']] * f_r['vehicles']

    # Defining start and end locations for vehicles
    f_r['starts'] = [0] * f_r['vehicles']
    f_r['ends'] = []
    if request['end_locations']:
        for end_location in request['end_locations']:
            if end_location == 'depot':
                f_r['ends'].append(0)
            else:
                idx = f_r['parcel_id'].index(end_location) + 1
                f_r['ends'].append(idx)
        while len(f_r['ends']) < f_r['vehicles']:
            f_r['ends'].append(len(f_r['lat']))
    else:
        f_r['ends'] = [len(f_r['lat'])] * f_r['vehicles']

    # obtaining cost matrix
    if request['billions_API']:
        f_r['cost_matrix'] = matrix.billions(request)
    else:
        f_r['cost_matrix'] = matrix.haversine(request)
    return f_r


# solve main depot request
def solve_md(f_req):
    # Format cost matrix
    C = f_req['cost_matrix']
    C = np.array(C) / 100
    C = C.astype(int)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(C),
                                           f_req['vehicles'],
                                           f_req['starts'],
                                           f_req['ends'])

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
        3000,  # vehicle maximum travel distance
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
        f_req['capacities'],  # vehicle maximum capacities
        True,  # start cumulative to zero
        'Capacity')

    # set up routes & distances lists to contain data for each search-strategy
    routes = []
    distances = []

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
        rts = [None] * f_req['vehicles']
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
                rts[vehicle_id] = np.delete(rts[vehicle_id], np.where(rts[vehicle_id] == f_req['n_deliveries'] + 1))

        # Calculate route distances and total distance
        dist = {}  # Creating empty distance dictionary
        total_distance = 0  # Initializing total distance
        for route_number, route in enumerate(rts):
            route_distance = 0
            for idx in range(len(route) - 1):
                route_distance += f_req['cost_matrix'][route[idx]][route[idx + 1]] / 10
            route_distance = round(route_distance, 1)
            dist['route' + str(route_number + 1)] = route_distance
            total_distance += route_distance
        dist['total'] = round(total_distance, 2)

        routes.append(rts)
        distances.append(dist['total'])
    # print(distances)

    for idx1, rt in enumerate(routes):
        for idx2, sub_rt in enumerate(rt):
            if sub_rt[0] == 0 and sub_rt[1] == 0:
                distances[idx1] = distances[idx1] * 10

    min_value = min(distances)
    index = distances.index(min_value)
    final_routes = routes[index]
    return final_routes


# get main depot response
def get_md_response(f_req, sol):
    rsp = {'status': 'OK', 'routes': []}  # Creating response dictionary
    for route_number, route in enumerate(sol):
        rt = []
        for idx, node in enumerate(route):
            picks = []
            drops = []
            address = f_req['address'][node]
            contact = f_req['contact'][node]
            if node == 0 and idx != len(route) - 1:  # if satisfied, node represents client
                for other_node in route:
                    if other_node > 0:
                        picks.append(f_req['parcel_id'][other_node - 1])
            elif node == 0 and idx == len(route) - 1:  # if satisfied, node represents client endpoint
                pass
            else:
                drops.append(f_req['parcel_id'][node - 1])
            node_info = {'address': address, 'contact': contact, 'picks': picks, 'drops': drops}
            rt.append(node_info)
        rsp['routes'].append(rt)
    return rsp





