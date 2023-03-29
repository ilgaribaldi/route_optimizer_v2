import numpy as np
from ortools.constraint_solver import pywrapcp
import pprint as pp
from utils import internal_solution_functions as isf
import math


# main depot request verification
def verify_md(request):
    rsp = 1
    n_deliveries = len(request['parcels'])
    parcel_id = [parcel['id'] for parcel in request['parcels']]
    total_parcel_volume = sum([obj['volume'] for obj in request['parcels']])
    total_vehicle_capacity = sum(v['capacity'] for v in request['vehicles'])

    # Check if total vehicle capacity is enough for all parcels
    if total_vehicle_capacity < total_parcel_volume:
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
            rsp = {'status': 400, 'body': [], 'total_distance': 1000000000,
                   'search_strategy': request['search_strategy']}
            break
    return rsp


# main depot request setup
def format_md(request):
    f_r = {
        'lat': [request["depot"]["lat"]] + [parcel['lat'] for parcel in request['parcels']],
        'lng': [request["depot"]['lng']] + [parcel['lng'] for parcel in request['parcels']],
        'address': [request["depot"]['address']] + [parcel['address'] for parcel in request['parcels']],
        'contact': [request["depot"]['contact']] + [parcel['contact'] for parcel in request['parcels']],
        'parcel_id': [parcel['id'] for parcel in request['parcels']],
        'n_deliveries': len(request['parcels']),
        'search_strategy': request['search_strategy'],
        'cost_matrix': request['cost_matrix'],
        'routeNumber': request['routeNumber'],
        'vehicle_ids': [v['id'] for v in request["vehicles"]]
    }

    demands = [obj['volume'] for obj in request['parcels']]
    vehicle_capacities = [v['capacity'] for v in request["vehicles"]]

    # --------------------- Choose vehicles based on vehicles requested + capacity--------------- #
    f_r["capacities"] = vehicle_capacities
    f_r['vehicles'] = len(request["vehicles"])
    # ------------------------------------------------------------------------------------------- #

    f_r['time'] = 2 if f_r['n_deliveries'] <= 25 else (3 if f_r['n_deliveries'] <= 50 else (
        6 if f_r['n_deliveries'] <= 75 else (15 if f_r['n_deliveries'] <= 150 else None)))

    # Fetch indexes for dummy nodes to ignore later on
    f_r['indexes_to_ignore'] = isf.indexes_to_kill(request)

    # Corresponding demands for dummy nodes
    end_location_demands = isf.get_end_location_demands(request)

    # Adding dummy nodes to demands
    demands = [0] + demands + end_location_demands + [0]
    f_r['demands'] = demands

    # Defining start and end locations for vehicles
    f_r['starts'] = [0] * f_r['vehicles']
    f_r['ends'] = [f_r['parcel_id'].index(end_location) + 1 if end_location != 'depot' else 0 for end_location in
                   request.get("end_locations", [])]
    f_r['ends'] += [len(f_r['lat'])] * (f_r['vehicles'] - len(f_r['ends']))

    print("number of vehicles:")
    print(f_r['vehicles'])

    return f_r


# solve main depot request
def solve_md(f_req):
    # Format cost matrix
    C = f_req['cost_matrix']
    C = np.array(C) / 10
    C = C.astype(int)

    data = {'distance_matrix': C, 'num_vehicles': f_req['vehicles'], 'depot': 0}

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(C),
        f_req['vehicles'],
        f_req['starts'],
        f_req['ends'],
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Use max vehicles
    if f_req["routeNumber"] == "max":
        # Add empty route constraint
        for vehicle_id in range(manager.GetNumberOfVehicles()):
            routing.SetVehicleUsedWhenEmpty(True, vehicle_id)

        count_dimension_name = 'count'
        routing.AddConstantDimension(
            1,  # increment by one every time
            f_req["n_deliveries"] + 2,  # make sure the return to depot node can be counted
            True,  # set count to zero
            count_dimension_name)
        count_dimension = routing.GetDimensionOrDie(count_dimension_name)
        count_dimension.SetGlobalSpanCostCoefficient(100)

        for veh in range(0, f_req["vehicles"]):
            index_end = routing.End(veh)
            count_dimension.SetCumulVarSoftLowerBound(index_end, 2, 100000)

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
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return f_req['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        f_req['capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Add Distance constraint.
    distance_limit = 500 if f_req['routeNumber'] == "min" else 450
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        distance_limit,  # vehicle maximum travel distance
        False,  # start cumulative to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    def print_solution(data, manager, routing, solution):
        """Prints solution on console."""
        print(f'Objective: {solution.ObjectiveValue()}')
        max_route_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += ' {} -> '.format(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(
                    previous_index, index, vehicle_id)
            plan_output += '{}\n'.format(manager.IndexToNode(index))
            plan_output += 'Distance of the route: {}m\n'.format(route_distance)
            print(plan_output)
            max_route_distance = max(route_distance, max_route_distance)
        print('Maximum of the route distances: {}m'.format(max_route_distance))



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

        print_solution(data, manager, routing, sol)

    except (AttributeError, TypeError, ValueError, NameError):
        return None, None

    return rts, total_distance


# get main depot response
def get_md_response(f_req, sol, distance):
    if sol is not None:
        rsp = {'status': 200, 'body': [], 'total_distance': distance, 'search_strategy': f_req['search_strategy']}
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
            route_dict = {
                "vehicle": f_req["vehicle_ids"][route_number],
                "route": rt
            }
            if len(rt) > 1:
                rsp['body'].append(route_dict)
    else:
        rsp = {'status': 204, 'body': [], 'total_distance': 1000000000, 'search_strategy': f_req['search_strategy']}
    return rsp
