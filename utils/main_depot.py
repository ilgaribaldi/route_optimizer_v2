from utils import matrix
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import pprint as pp
from utils import internal_solution_functions as isf


# main depot request verification
def verify_md(request):
    n_deliveries = len(request['parcels'])
    parcel_id = []
    for parcel in request['parcels']:
        parcel_id.append(parcel['id'])
    rsp = 1

    # Calculating total vehicle capacity
    vehicle_capacities = [5, 10, 15]
    vehicles = [
        request['available_vehicles']['motorcycles'],
        request['available_vehicles']['cars'],
        request['available_vehicles']['vans']
    ]

    total_possible_capacity = 0
    for idx, vehicle in enumerate(vehicles):
        total_possible_capacity += vehicle_capacities[idx] * vehicle

    total_parcel_volume = 0
    for obj in request['parcels']:
        total_parcel_volume += obj['volume']

    # Check if total vehicle capacity is enough for all parcels
    if total_possible_capacity < total_parcel_volume:
        rsp = {'status': 400}

    '''
    # Check if depot_return > vehicle number
    
    if len(request['end_locations']) > request['vehicles']:
        rsp = {'status': 400}
        
    if request['vehicles'] > n_deliveries:
        rsp = {'status': 400}
    '''

    if n_deliveries > 150:
        rsp = {'status': "400: too many packages for optimizer"}

    for end_location in request['end_locations']:
        if end_location != 'depot' and end_location not in parcel_id:
            rsp = {'status': 400}
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

    # Calculating vehicles used based on total volume of parcels
    vehicle_capacities = [5, 10, 15]
    vehicles = [
        request['available_vehicles']['motorcycles'],
        request['available_vehicles']['cars'],
        request['available_vehicles']['vans']
    ]
    vehicles_used = [0, 0, 0]

    total_volume = 0
    for obj in request['parcels']:
        total_volume += obj['volume']
    total_volume_left = total_volume

    for idx, vehicle_quantity in enumerate(vehicles):
        if total_volume_left > 0:
            if vehicle_quantity > 0:
                for i in range(1, vehicle_quantity + 1):
                    if i * vehicle_capacities[idx] >= total_volume_left:
                        vehicles_used[idx] = i
                        break
                    if vehicles_used[idx] == 0:
                        vehicles_used[idx] = vehicle_quantity
        total_volume_left = max(total_volume_left - vehicles_used[idx] * vehicle_capacities[idx], 0)

    # Defining vehicle capacities
    capacities = []
    for idx, vehicles in enumerate(vehicles_used):
        for i in range(vehicles):
            capacities.append(vehicle_capacities[idx])
    f_r['capacities'] = capacities

    # Additional data
    f_r['n_deliveries'] = len(request['parcels'])
    f_r['vehicles'] = sum(vehicles_used)
    f_r['search_strategy'] = request['search_strategy']
    f_r['cost_matrix'] = request['cost_matrix']

    if f_r['n_deliveries'] <= 25:  # 10 seconds
        f_r['time'] = 3   # 3
    elif f_r['n_deliveries'] <= 50:  # 15 seconds
        f_r['time'] = 3
    elif f_r['n_deliveries'] <= 75:  # 20 seconds
        f_r['time'] = 4
    elif f_r['n_deliveries'] <= 100:  # 25 seconds
        f_r['time'] = 6
    elif f_r['n_deliveries'] <= 150:  # 27 seconds
        f_r['time'] = 9

    '''
    If end locations exist and ar different from "depot", we need to duplicate end location nodes
    with their corresponding demands and delete them later on. 
    '''

    # Fetch indexes for dummy nodes to ignore later on
    f_r['indexes_to_ignore'] = isf.indexes_to_kill(request)

    # Corresponding demands for dummy nodes
    end_location_demands = []
    if 'end_locations' in request.keys():
        if 'depot' in request['end_locations']:
            special_case = not all(end_location == 'depot' for end_location in request['end_locations'])
        else:
            special_case = False

        if not special_case:
            if "end_locations" in request.keys():
                if request["end_locations"]:
                    for ID in request['end_locations']:
                        if ID != 'depot':
                            for idx, obj in enumerate(request['parcels']):
                                if ID == obj['id']:
                                    end_location_demands.append(obj['volume'])
        else:
            if "end_locations" in request.keys():
                if request["end_locations"]:
                    for end_location in request['end_locations']:
                        if end_location != 'depot':
                            for idx, obj in enumerate(request['parcels']):
                                if end_location == obj['id']:
                                    end_location_demands.append(obj['volume'])
                        else:
                            end_location_demands.append(0)

    # Defining location demands
    demands = []
    for obj in request['parcels']:
        demands.append(obj['volume'])
    demands = [0] + demands + end_location_demands + [0]
    f_r['demands'] = demands

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

    return f_r


# solve main depot request
def solve_md(f_req):
    # Format cost matrix
    C = f_req['cost_matrix']
    C = np.array(C) / 100
    C = C.astype(int)

    data = {
        "demands": f_req['demands'],
        "vehicle_capacities": f_req['capacities'],
        "num_vehicles": f_req['vehicles'],
        "depot": 0
    }

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(C),
                                           f_req['vehicles'],
                                           f_req['starts'],
                                           f_req['ends'],
                                           )

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

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demand NodeIndex.
        from_node = manager.IndexToNode(from_index)
        # print(f_req['demands'][from_node], from_node)
        # print('-------------------------------------')
        return f_req['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        f_req['capacities'],  # vehicle maximum capacities
        True,  # start cumulative to zero
        'Capacity')

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        100000,  # vehicle maximum travel distance
        True,  # start cumulative to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    try:
        # Define search parameters
        search_parameters = isf.choose_search_parameters(f_req['time'], f_req['search_strategy'])

        # Solve the problem.
        sol = routing.SolveWithParameters(search_parameters)

        # print solution
        # isf.print_solution(data, manager, routing, sol)

        # Generate route arrays
        rts = isf.get_route_arrays(f_req, routing, sol, manager)

        # Calculate route distances and total distance
        total_distance = isf.get_total_distance(f_req, rts)

        for idx2, sub_rt in enumerate(rts):
            if sub_rt[0] == 0 and sub_rt[1] == 0:
                total_distance = total_distance * 10

        return rts, total_distance
    except AttributeError:
        return None, None
    except TypeError:
        return None, None


# get main depot response
def get_md_response(f_req, sol, distance):
    if sol is not None:
        rsp = {'status': 200, 'routes': [], 'total_distance': distance, 'search_strategy': f_req['search_strategy']}
        for route_number, route in enumerate(sol):
            rt = []
            for idx, node in enumerate(route):
                if node in f_req['indexes_to_ignore']:
                    continue
                picks = []
                drops = []
                address = f_req['address'][node]
                contact = f_req['contact'][node]
                if node == 0 and idx != len(route) - 1:  # if satisfied, node represents client
                    for other_node in route:
                        if other_node in f_req['indexes_to_ignore']:
                            continue
                        if other_node > 0:
                            picks.append(f_req['parcel_id'][other_node - 1])
                elif node == 0 and idx == len(route) - 1:  # if satisfied, node represents client endpoint
                    pass
                else:
                    drops.append(f_req['parcel_id'][node - 1])
                node_info = {'address': address, 'contact': contact, 'picks': picks, 'drops': drops}
                rt.append(node_info)
            rsp['routes'].append(rt)
    else:
        rsp = {'status': 204}
    return rsp





