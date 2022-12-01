import haversine as hs
import requests
import numpy as np
import pprint as pp
from utils import internal_solution_functions as isf


# Haversine cost-matrix (Updated to allow end_locations)
def haversine(request):
    lat = []
    lng = []

    lat.append(request['lat'])
    lng.append(request['lng'])

    if 'parcels' in request.keys():
        locations = request['parcels']
    else:
        locations = request['depots']

    for obj in locations:
        lat.append(obj['lat'])
        lng.append(obj['lng'])

    indexes = []
    if 'end_locations' in request.keys():
        if 'depot' in request['end_locations']:
            special_case = not all(end_location == 'depot' for end_location in request['end_locations'])
        else:
            special_case = False

        if not special_case:
            if request["end_locations"]:
                for ID in request['end_locations']:
                    if ID != 'depot':
                        for idx, obj in enumerate(request['parcels']):
                            if ID == obj['id']:
                                indexes.append(idx + 1)
        else:
            if request["end_locations"]:
                for end_location in request['end_locations']:
                    if end_location == 'depot':
                        indexes.append(0)
                    else:
                        for idx, obj in enumerate(request['parcels']):
                            if end_location == obj['id']:
                                indexes.append(idx + 1)

    lat_lng = list(zip(lat, lng))

    C = []
    for j, row in enumerate(lat_lng):
        row = []
        for i, col in enumerate(lat_lng):
            d = (hs.haversine(lat_lng[j], lat_lng[i], unit=hs.Unit.METERS)) / 10
            row.append(d)
        for idx in indexes:
            row.append(row[idx])
        row.append(0)
        C.append(row)
    for idx in indexes:
        C.append(C[idx])
    C.append([0] * len(C[0]))
    return C


# NextBillion API cost-matrix (Updated to allow end_locations)
def billions(request):
    # Define data type
    if 'vehicles' in request.keys():
        data_type = 'distance'
    else:
        data_type = 'duration'

    if 'parcels' in request.keys():
        locations = request['parcels']
    else:
        locations = request['depots']

    # Generate origin and destination strings for request
    origins = str(request['lat']) + "," + str(request['lng'])
    destinations = str(request['lat']) + "," + str(request['lng'])
    for idx, obj in enumerate(locations):
        origins += "|" + str(obj['lat']) + "," + str(obj['lng'])
        destinations += "|" + str(obj['lat']) + "," + str(obj['lng'])

    api_key = "BILLIONS_API_KEY"
    begin = "https://api.nextbillion.io/distancematrix/json?origins="
    end = "&destinations="
    mode = "&mode=car&key="

    url = begin + origins + end + destinations + mode + api_key
    output = requests.get(url).json()

    indexes = []
    if 'end_locations' in request.keys():
        if 'depot' in request['end_locations']:
            special_case = not all(end_location == 'depot' for end_location in request['end_locations'])
        else:
            special_case = False

        if not special_case:
            if request["end_locations"]:
                for ID in request['end_locations']:
                    if ID != 'depot':
                        for idx, obj in enumerate(request['parcels']):
                            if ID == obj['id']:
                                indexes.append(idx + 1)
        else:
            if request["end_locations"]:
                for end_location in request['end_locations']:
                    if end_location == 'depot':
                        indexes.append(0)
                    else:
                        for idx, obj in enumerate(request['parcels']):
                            if end_location == obj['id']:
                                indexes.append(idx + 1)
    print(indexes)

    # Populate matrix with response
    C = []
    for obj in output['rows']:
        row = []
        for data in obj['elements']:
            row.append(data[data_type]['value'])
        for idx in indexes:
            row.append(row[idx])
        row.append(0)
        C.append(row)
    for idx in indexes:
        C.append(C[idx])
    C.append([0] * len(C[0]))
    return C


# Google API cost-matrix
def google(request):
    # Define data type
    if 'vehicles' in request.keys():
        data_type = 'distance'
    else:
        data_type = 'duration'

    if 'parcels' in request.keys():
        locations = request['parcels']
    else:
        locations = request['depots']

    # Generate origin and destination strings for request
    origin = str(request['lat']) + " " + str(request['lng'])
    destinations = str(locations[0]['lat']) + " " + str(locations[0]['lng'])
    C = []

    for idx, obj in enumerate(locations):
        if idx > 0:
            destinations += "|" + str(obj['lat']) + " " + str(obj['lng'])

    api_key = "GOOGLE_API_KEY"
    start = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
    end = "&destinations="
    mode = "&mode=car&key="

    url = start + origin + end + destinations + mode + api_key
    output = requests.get(url).json()

    for obj in output['rows']:
        row = [0]
        for data in obj['elements']:
            row.append(data[data_type]['value'])
        row.append(0)
        C.append(row)

    for idx1, start_node in enumerate(locations):
        origin = str(start_node['lat']) + " " + str(start_node['lng'])
        destinations = str(request['lat']) + " " + str(request['lng'])
        for idx2, obj in enumerate(locations):
            if idx1 == idx2:
                pass
            else:
                destinations += "|" + str(obj['lat']) + " " + str(obj['lng'])
        url = start + origin + end + destinations + mode + api_key
        output = requests.get(url).json()

        for obj in output['rows']:
            row = []
            for data in obj['elements']:
                row.append(data[data_type]['value'])
            row.insert(idx1 + 1, 0)
            row.append(0)
            C.append(row)
    C.append([0] * len(C[0]))
    return C


# Multi-Depot Haversine (Requires different calculations)
def multi_depot_haversine(request):
    lat_lng = isf.get_multi_depot_location_array(request)
    C = []

    for j in range(len(lat_lng)):
        row = []
        if j == 0:
            row = [0] * len(lat_lng)
        else:
            for i in range(len(lat_lng)):
                d = (hs.haversine(lat_lng[j], lat_lng[i], unit=hs.Unit.METERS)) / 100
                row.append(d)
                row[0] = 0
        C.append(row)
    return C

