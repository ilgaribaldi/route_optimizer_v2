from ortools.constraint_solver import pywrapcp
import numpy as np
from ortools.constraint_solver import routing_enums_pb2


# Generate route arrays
def get_route_arrays(f_req, routing, solution, manager):
    rts = [None] * f_req['vehicles']
    rts = np.array(rts)
    if solution:
        for vehicle_id in range(f_req['vehicles']):
            rts[vehicle_id] = 0
            previous_index = routing.Start(vehicle_id)
            while not routing.IsEnd(previous_index):
                index = solution.Value(routing.NextVar(previous_index))
                end_node = manager.IndexToNode(index)
                rts[vehicle_id] = np.append(rts[vehicle_id], end_node)
                previous_index = index
            # Deleting dummy nodes
            if "lat_lng" not in f_req.keys():
                rts[vehicle_id] = np.delete(rts[vehicle_id], np.where(rts[vehicle_id] == f_req['n_deliveries'] + 1))
            else:
                rts[vehicle_id] = np.delete(rts[vehicle_id], np.where(rts[vehicle_id] == 0))

        # ------------------------------ Multi Depot Requests Only ------------------------------ #
        if "lat_lng" in f_req.keys():
            # Rewriting solution with "real nodes" (client nodes will be represented as negative)
            client_idx = 0
            rts = rts - f_req['total_deliveries']
            for vehicle_id in range(len(rts)):
                for node_idx in range(len(rts[vehicle_id])):
                    node = rts[vehicle_id][node_idx]
                    if node + f_req['total_deliveries'] <= f_req['total_deliveries']:  # If condition is satisfied;
                        for idx in range(len(f_req['cum_del']) - 1):  # node represents client
                            if f_req['cum_del'][idx] < node + f_req['total_deliveries'] <= f_req['cum_del'][idx + 1]:
                                client_idx = idx + 1
                        rts[vehicle_id][node_idx] = -client_idx
                # Deleting cloned nodes
                indexes = np.unique(rts[vehicle_id], return_index=True)[1]
                rts[vehicle_id] = np.array([rts[vehicle_id][idx] for idx in sorted(indexes)])
    return rts


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))


def choose_search_parameters(time, search_strategy):

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    if search_strategy == 1:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    elif search_strategy == 2:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC)
    elif search_strategy == 3:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.FIRST_UNBOUND_MIN_VALUE)
    elif search_strategy == 4:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_ARC)
    elif search_strategy == 5:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES)
    elif search_strategy == 6:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)
    elif search_strategy == 7:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION)
    elif search_strategy == 8:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.SAVINGS)
    elif search_strategy == 9:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.BEST_INSERTION)
    elif search_strategy == 10:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.ALL_UNPERFORMED)

    # MIGHT RUN FOREVER
    elif search_strategy == 11:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.GLOBAL_CHEAPEST_ARC)

    if time == 0:  # If condition is satisfied, return optimal solution as fast as possible
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC)
    else:  # If condition is not satisfied, return solution as fast as possible or when time runs out
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)  # GUIDED_LOCAL_SEARCH
        search_parameters.time_limit.FromSeconds(time)

    return search_parameters


def get_total_distance(f_req, rts):
    if "lat_lng" not in f_req.keys():
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
    else:
        # Rewriting solution with correct indexes for cost matrix
        matrix_sol = [None] * f_req['vehicles']
        matrix_sol = np.array(matrix_sol)
        for vehicle_id in range(f_req['vehicles']):
            for node_idx in range(len(rts[vehicle_id])):
                if rts[vehicle_id][node_idx] > 0:
                    idx = rts[vehicle_id][node_idx] + f_req['total_deliveries']
                else:
                    idx = f_req['cum_del'][-rts[vehicle_id][node_idx]]
                matrix_sol[vehicle_id] = np.append(matrix_sol[vehicle_id], idx)
            matrix_sol[vehicle_id] = np.delete(matrix_sol[vehicle_id], 0)

        # Obtaining distance for each route and storing answers in dictionary
        dist = {}  # Creating empty distance dictionary
        total_distance = 0  # Initializing total distance
        route_num = 1  # Initializing route number
        for vehicle_id in range(f_req['vehicles']):
            route_distance = 0
            for idx in range(len(matrix_sol[vehicle_id]) - 1):
                route_distance += f_req['cost_matrix'][matrix_sol[vehicle_id][idx]][
                                      matrix_sol[vehicle_id][idx + 1]] / 10
            dist['route' + str(route_num)] = route_distance
            total_distance += route_distance
            route_num += 1
        dist['total'] = total_distance
    return dist['total']


def indexes_to_kill(request):
    indexes_to_ignore = []
    if 'end_locations' in request.keys():
        if 'depot' in request['end_locations']:
            special_case = not all(end_location == 'depot' for end_location in request['end_locations'])
        else:
            special_case = False
        if not special_case:
            if request['end_locations']:
                index = len(request['parcels']) + 1
                indexes_to_ignore.append(index)
                for end_location in request['end_locations']:
                    if end_location != 'depot':
                        index += 1
                        indexes_to_ignore.append(index)
        else:
            if request['end_locations']:
                index = len(request['parcels']) + 1
                indexes_to_ignore.append(index)
                for end_location in request['end_locations']:
                    index += 1
                    indexes_to_ignore.append(index)
    return indexes_to_ignore


def get_multi_depot_location_array(request):
    deliveries_lat = []
    deliveries_lng = []
    client_lat = []
    client_lng = []
    n_deliveries = []
    clients = len(request['locations'])

    for client in request['locations']:
        client_lat.append(client['lat'])
        client_lng.append(client['lng'])
        n_deliveries.append(len(client['parcels']))
        for parcel in client['parcels']:
            deliveries_lat.append(parcel['lat'])
            deliveries_lng.append(parcel['lng'])

    # Joining (latitude, longitude)
    lat_lng = list(zip(deliveries_lat, deliveries_lng))

    # Cloning nodes for pickups-deliveries trick
    if clients > 1:
        for i in range(clients):
            lat_c = np.ones(n_deliveries[-1 - i], dtype=int) * client_lat[-1 - i]
            lng_c = np.ones(n_deliveries[-1 - i], dtype=int) * client_lng[-1 - i]
            lat_lng_c = list(zip(lat_c, lng_c))
            lat_lng = np.concatenate((lat_lng_c, lat_lng))
    else:
        lat_c = np.ones(n_deliveries[0], dtype=int) * client_lat
        lng_c = np.ones(n_deliveries[0], dtype=int) * client_lng
        lat_lng_c = list(zip(lat_c, lng_c))
        lat_lng = np.concatenate((lat_lng_c, lat_lng))

    # Creating dummy initial point and adding it to list
    lat_lng_d = [[0, 0]]
    lat_lng = np.concatenate((lat_lng_d, lat_lng))

    return lat_lng

