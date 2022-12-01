import haversine as hs
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
from matplotlib import pyplot as plt
from utils import matrix
import pprint as pp
from utils import internal_solution_functions as isf


# Format initial request
def format_mud(request):
    f_r = {}  # Dictionary containing everything

    deliveries_lat = []  # Will contain all delivery latitudes
    deliveries_lng = []  # Will contain all delivery longitudes
    deliveries_address = []  # Will contain all delivery addresses
    deliveries_contact = []  # Will contain all delivery contacts

    client_lat = []  # Will contain all client latitudes
    client_lng = []  # Will contain all client longitudes
    client_address = []  # Will contain all client addresses
    client_contact = []  # Will contain all client contacts

    parcel_id = []  # Will contain all parcel ids
    n_deliveries = []  # Will contain number of deliveries for each client
    client_number = []  # Will contain corresponding client number for each parcel

    clients = len(request['locations']) # Number of clients
    vehicles = 1  # Number of vehicles
    capacities = [40] * vehicles  # List containing (parcel) capacity per vehicle (could be volume)
    pickups_deliveries = []  # List of lists with pickup node and delivery node
    demands = [0]  # List that will contain demand (or weight) of each parcel
    cumulative_deliveries = [0]  # List containing cumulative deliveries divided by client

    # Populating latitude, longitude, address, and contact lists
    c_aux = 1
    for client in request['locations']:
        client_lat.append(client['lat'])
        client_lng.append(client['lng'])
        client_address.append(client['address'])
        client_contact.append(client['contact'])
        n_deliveries.append(len(client['parcels']))
        for parcel in client['parcels']:
            deliveries_lat.append(parcel['lat'])
            deliveries_lng.append(parcel['lng'])
            deliveries_address.append(parcel['address'])
            deliveries_contact.append(parcel['contact'])
            client_number.append(c_aux)
            parcel_id.append(parcel['id'])
        c_aux += 1

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

    s = 0  # variable that stores cumulative sum of deliveries
    for element in n_deliveries:
        s += element
        cumulative_deliveries.append(s)

    # Defining Pickups & Deliveries, and Demands
    h = len(deliveries_lat)
    for i in range(1, h + 1):
        pickups_deliveries.append([i, h + i])
        demands.append(1)
    for i in range(h):
        demands.append(-1)

    # Defining search strategy (6, 7, 8, 11)
    if request['search_strategy'] == 1:
        f_r['search_strategy'] = 6
    elif request['search_strategy'] == 2:
        f_r['search_strategy'] = 7
    elif request['search_strategy'] == 3:
        f_r['search_strategy'] = 8
    elif request['search_strategy'] == 4:
        f_r['search_strategy'] = 11
    else:
        f_r['search_strategy'] = 6

    # Calculating cost matrix
    f_r['cost_matrix'] = request['cost_matrix']

    # Deliveries info
    f_r['deliveries_lat'] = deliveries_lat
    f_r['deliveries_lng'] = deliveries_lng
    f_r['deliveries_address'] = deliveries_address
    f_r['deliveries_contact'] = deliveries_contact
    f_r['n_deliveries'] = n_deliveries
    f_r['parcel_id'] = parcel_id
    f_r['cum_del'] = cumulative_deliveries
    f_r['total_deliveries'] = len(deliveries_lat)

    # Client info
    f_r['client_lat'] = client_lat
    f_r['client_lng'] = client_lng
    f_r['client_address'] = client_address
    f_r['client_contact'] = client_contact
    f_r['client_number'] = client_number

    # Concatenated client and delivery cloned info
    f_r['lat_lng'] = lat_lng

    # Additional info
    f_r['pickups_deliveries'] = pickups_deliveries
    f_r['capacities'] = capacities
    f_r['demands'] = demands
    f_r['vehicles'] = vehicles
    f_r['time'] = request['time']

    return f_r


# solve multi depot request
def solve_mud(f_req):
    C = f_req['cost_matrix']
    C = np.array(C)
    C = C.astype(int)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(C),
                                           f_req['vehicles'],
                                           0)

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return f_req['cost_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        30000,  # vehicle maximum travel distance
        True,  # start cumulative to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Define Transportation Requests.
    for req in f_req['pickups_deliveries']:
        pickup_index = manager.NodeToIndex(req[0])
        delivery_index = manager.NodeToIndex(req[1])
        routing.AddPickupAndDelivery(pickup_index, delivery_index)
        routing.solver().Add(
            routing.VehicleVar(pickup_index) == routing.VehicleVar(
                delivery_index))
        routing.solver().Add(
            distance_dimension.CumulVar(pickup_index) <=
            distance_dimension.CumulVar(delivery_index))

    '''
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
    '''

    # Setting first solution heuristic (6, 7, 8, 11)
    search_parameters = isf.choose_search_parameters(f_req['time'], f_req['search_strategy'])

    # Solve the problem
    sol = routing.SolveWithParameters(search_parameters)

    # Generate route arrays
    rts = isf.get_route_arrays(f_req, routing, sol, manager)

    # Calculate route distance and total distance
    total_distance = isf.get_total_distance(f_req, rts)
    # print(total_distance)

    return rts, total_distance


# get multi depot response
def get_mud_response(f_req, sol, distance):
    # Defining search strategy (6, 7, 8, 11)
    search_strategy = 0
    if f_req['search_strategy'] == 6:
        search_strategy = 1
    elif f_req['search_strategy'] == 7:
        search_strategy = 2
    elif f_req['search_strategy'] == 8:
        search_strategy = 3
    elif f_req['search_strategy'] == 11:
        search_strategy = 4

    if sol is not None:
        rsp = {'status': 200, 'route': [], 'total_distance': distance, "search_strategy": search_strategy}
        for node in sol[0]:
            picks = []
            drops = []
            if node < 0:  # if condition is satisfied, node represents client
                idx = -node - 1
                address = f_req['client_address'][idx]
                contact = f_req['client_contact'][idx]
                for other_node in sol[0]:
                    if other_node > 0:
                        idx = other_node - 1
                        if f_req['client_number'][idx] == -node:
                            picks.append(f_req['parcel_id'][idx])
            else:  # if condition is not satisfied, node represents delivery
                idx = node - 1
                address = f_req['deliveries_address'][idx]
                contact = f_req['deliveries_contact'][idx]
                drops.append(f_req['parcel_id'][idx])
            node_info = {'address': address, 'contact': contact, 'picks': picks, 'drops': drops}
            rsp['route'].append(node_info)
    else:
        rsp = {'status': 204}
    return rsp


# plot solution to verify
def plot_solution(f_req, sol):
    # Plotting client nodes and their corresponding deliveries
    clients = list(range(1, len(f_req['client_lat']) + 1))
    plt.scatter(x=f_req['deliveries_lng'], y=f_req['deliveries_lat'],
                c=f_req['client_number'], cmap='viridis', s=50)
    plt.scatter(x=f_req['client_lng'], y=f_req['client_lat'],
                c=clients, cmap='viridis', marker='^', s=200)

    # Annotating nodes and plotting routes
    for vehicle_id in range(len(sol)):
        route_lat = []
        route_lng = []
        for node in sol[vehicle_id]:
            if node > 0:
                plt.annotate(str(node),
                             xy=(f_req['deliveries_lng'][node - 1], f_req['deliveries_lat'][node - 1] + 0.00001))
                route_lat.append(f_req['deliveries_lat'][node - 1])
                route_lng.append(f_req['deliveries_lng'][node - 1])
            else:
                plt.annotate(str([-node]),
                             xy=(f_req['client_lng'][-node - 1], f_req['client_lat'][-node - 1] + 0.00001))
                route_lat.append(f_req['client_lat'][-node - 1])
                route_lng.append(f_req['client_lng'][-node - 1])
        plt.plot(route_lng, route_lat)

        # Plotting directional arrows
        lat0 = np.array(route_lat[0:-1])
        lat1 = np.array(route_lat[1:])
        lng0 = np.array(route_lng[0:-1])
        lng1 = np.array(route_lng[1:])
        lat_pos = (lat0 + lat1) / 2
        lng_pos = (lng0 + lng1) / 2
        lat_dir = lat1 - lat0
        lng_dir = lng1 - lng0
        for LAT, LNG, dLAT, dLNG in zip(lat_pos, lng_pos, lat_dir, lng_dir):
            plt.annotate("", xytext=(LNG, LAT), xy=(LNG + 0.001 * dLNG, LAT + 0.001 * dLAT),
                         arrowprops=dict(arrowstyle="->", color='k'), size=8)
    plt.show()