from utils import matrix
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math
from utils import internal_solution_functions as isf


# recollections request verification
def verify_rec(req):
    n_locations = len(req['depots'])
    rsp = 1

    if req['method'] != 'google' and req['method'] != 'billions' and req['method'] != "haversine":
        rsp = {'status': 400, 'body': []}

    if req['method'] == 'google' and n_locations > 25:
        rsp = {'status': 400, 'body': []}

    return rsp


# recollections request setup
def format_rec(request):
    f_r = {'lat': [], 'lng': [], 'address': [], 'contact': [], 'depot_id': [], 'parcels': []}

    # Depot data
    f_r['lat'].append(request["depot"]['lat'])
    f_r['lng'].append(request["depot"]['lng'])
    f_r['address'].append(request["depot"]['address'])
    f_r['contact'].append(request["depot"]['contact'])

    # Clients data
    for depot in request['depots']:
        f_r['lat'].append(depot['lat'])
        f_r['lng'].append(depot['lng'])
        f_r['address'].append(depot['address'])
        f_r['contact'].append(depot['contact'])
        f_r['depot_id'].append(depot['id'])
        f_r['parcels'].append(depot['parcels'])

    # Additional data
    f_r['method'] = request['method']
    f_r['search_strategy'] = request['search_strategy']
    f_r['cost_matrix'] = request['cost_matrix']
    f_r['n_locations'] = len(request['depots'])

    # Defining search strategies
    if f_r['n_locations'] <= 25:  # 10 seconds
        f_r['time'] = 1
        f_r['trials'] = 4
    elif f_r['n_locations'] <= 50:  # 15 seconds
        f_r['time'] = 2
        f_r['trials'] = 5

    # Defining location demands
    f_r['demands'] = [0] + [1] * f_r['n_locations'] + [0]
    f_r['vehicles'] = len(request['vehicles'])
    f_r['vehicle_ids'] = [v['id'] for v in request["vehicles"]]

    return f_r


# solve recollections request
def solve_rec(f_req):
    # Define max time per route
    if f_req['method'] == 'google':
        max_cost = 3000
    elif f_req['method'] == 'billions':
        max_cost = 2500
    else:
        max_cost = 2000

    # Define cost matrix
    C = f_req['cost_matrix']

    # Create lists to store solution
    final_times = []
    final_routes = []

    vehicles = f_req['vehicles']
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
        max_cost,  # vehicle maximum travel time
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

    # Add empty route constraint
    for vehicle_id in range(manager.GetNumberOfVehicles()):
        routing.SetVehicleUsedWhenEmpty(True, vehicle_id)

    count_dimension_name = 'count'
    routing.AddConstantDimension(
        1,  # increment by one every time
        len(f_req['lat']) + 2,  # make sure the return to depot node can be counted
        True,  # set count to zero
        count_dimension_name)
    count_dimension = routing.GetDimensionOrDie(count_dimension_name)
    count_dimension.SetGlobalSpanCostCoefficient(100)

    for veh in range(0, vehicles):
        index_end = routing.End(veh)
        count_dimension.SetCumulVarSoftLowerBound(index_end, 2, 100000)

    # set up routes & times lists to contain data for each search-strategy
    routes = []
    times = []
    rt_times = []

    # Define search parameters
    search_parameters = isf.choose_search_parameters(f_req['time'], f_req['search_strategy'])

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


# get recollections response
def get_rec_response(f_req, sol):
    if sol is not None:
        rsp = {'status': 200, 'body': []}  # Creating response dictionary
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
                        seconds = f_req['cost_matrix'][route[idx - 1]][route[idx]]
                        time = round(seconds / 60, 2)
                    if node == 0:  # if satisfied, node represents main depot
                        for other_node in route:
                            if other_node > 0:
                                drops += f_req['parcels'][other_node - 1]
                    else:
                        picks = f_req['parcels'][node - 1]

                    node_info = {'address': address,
                                 'contact': contact,
                                 'picks': picks,
                                 'drops': drops,
                                 'timeToStop': time}

                    rt.append(node_info)
                route_dict = {
                    "vehicle": f_req["vehicle_ids"][route_number],
                    "route": rt
                }
                if len(rt) > 1:
                    rsp['body'].append(route_dict)
    else:
        rsp = {'status': 402, 'body': []}
    return rsp
