from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


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
    return plt


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
        for idx, parcel in enumerate(route):
            if idx > 0:
                ids.append(parcel['drops'][0])

        plt.scatter(np.array(lng[1:]), np.array(lat[1:]))
        plt.plot(np.array(lng), np.array(lat))

        for idx, lt in enumerate(lat):
            if idx > 0:
                plt.annotate(ids[idx-1], xy=(lng[idx], lat[idx] + 0.00001))

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