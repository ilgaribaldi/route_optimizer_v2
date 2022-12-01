from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pprint as pp


# get solution plot
def solution(f_req, sol):
    sns.set(style="dark")
    plt.figure(1)
    # Plotting client location
    plt.scatter(x=f_req['lng'][0], y=f_req['lat'][0], c='k', marker='^', s=200)

    # Plotting delivery locations
    plt.scatter(x=f_req['lng'][1:], y=f_req['lat'][1:], c='r', s=50)

    # Annotating nodes
    for idx, lat in enumerate(f_req['lat']):
        if idx > 0:
            plt.annotate(str(idx), xy=(f_req['lng'][idx], f_req['lat'][idx] + 0.00001))

    # Plotting routes
    for route in sol:
        plt.plot(np.array(f_req['lng'])[route], np.array(f_req['lat'])[route])

    # Plotting directional arrows
    for route in sol:
        lat0 = np.array(f_req['lat'])[route[0:-1]]
        lat1 = np.array(f_req['lat'])[route[1:]]
        lng0 = np.array(f_req['lng'])[route[0:-1]]
        lng1 = np.array(f_req['lng'])[route[1:]]
        lat_pos = (lat0 + lat1) / 2
        lng_pos = (lng0 + lng1) / 2
        lat_dir = lat1 - lat0
        lng_dir = lng1 - lng0
        for LAT, LNG, dLAT, dLNG in zip(lat_pos, lng_pos, lat_dir, lng_dir):
            plt.annotate("", xytext=(LNG, LAT), xy=(LNG + 0.001 * dLNG, LAT + 0.001 * dLAT),
                         arrowprops=dict(arrowstyle="->", color='k'), size=8)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    return plt


# get multi-depot solution plot
def mud_solution(f_req, sol):
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

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()


# get response plot
def response(rsp):
    plt.figure(1)
    sns.set(style="dark")

    # Plotting client location
    client_lat = float(rsp['routes'][0][0]['address']['location']['coordinates'][0])
    client_lng = float(rsp['routes'][0][0]['address']['location']['coordinates'][1])
    plt.scatter(x=client_lng, y=client_lat, c='k', marker='^', s=200)
    for route in rsp['routes']:
        lat = [float(i['address']['location']['coordinates'][0]) for i in route if 'address' in i]
        lng = [float(i['address']['location']['coordinates'][1]) for i in route if 'address' in i]
        ids = []
        volumes = []

        for idx, location in enumerate(route):
            if idx > 0:
                if 'drops' in location.keys() and location['drops']:
                    ids.append(location['drops'][0])
                else:
                    ids.append("")

        plt.scatter(np.array(lng[1:]), np.array(lat[1:]))
        plt.plot(np.array(lng), np.array(lat))

        for idx, lt in enumerate(lat):
            if 0 < idx:
                plt.annotate(ids[idx - 1], xy=(lng[idx], lat[idx] + 0.00001))

        lat0 = np.array(lat[0:-1])
        lat1 = np.array(lat[1:])
        lng0 = np.array(lng[0:-1])
        lng1 = np.array(lng[1:])
        lat_pos = (lat0 + lat1) / 2
        lng_pos = (lng0 + lng1) / 2
        lat_dir = lat1 - lat0
        lng_dir = lng1 - lng0
        for LAT, LNG, dLAT, dLNG in zip(lat_pos, lng_pos, lat_dir, lng_dir):
            plt.annotate("", xytext=(LNG, LAT), xy=(LNG + 0.001 * dLNG, LAT + 0.001 * dLAT),
                         arrowprops=dict(arrowstyle="->", color='k'), size=8)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    return plt


# get cluster plot
def clusters(f_req, req_clusters):
    plt.figure(2)
    sns.set(style="dark")
    sns.scatterplot(
        x=f_req['lng'][1:],
        y=f_req['lat'][1:],
        hue=req_clusters,
        palette="deep",
        style=req_clusters,
    )

    # Plotting client location
    plt.scatter(x=f_req['lng'][0], y=f_req['lat'][0], c='k', marker='^', s=200)
    return plt


