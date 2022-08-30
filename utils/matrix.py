import haversine as hs
import requests


# Haversine cost-matrix
def haversine(request):
    lat = []
    lng = []

    lat.append(request['lat'])
    lng.append(request['lng'])

    for package in request['parcels']:
        lat.append(package['lat'])
        lng.append(package['lng'])

    lat_lng = list(zip(lat, lng))

    C = []
    for j, row in enumerate(lat_lng):
        row = []
        for i, col in enumerate(lat_lng):
            d = (hs.haversine(lat_lng[j], lat_lng[i], unit=hs.Unit.METERS))
            row.append(d)
        row.append(0)
        C.append(row)
    C.append([0] * len(C[0]))
    return C


# NextBillion API cost-matrix
def billions(request):
    # Define data type
    if len(request) == 6:
        data_type = 'duration'
    else:
        data_type = 'distance'

    # Generate origin and destination strings for request
    origins = str(request['lat']) + "," + str(request['lng'])
    destinations = str(request['lat']) + "," + str(request['lng'])
    for idx, parc in enumerate(request['parcels']):
        origins += "|" + str(parc['lat']) + "," + str(parc['lng'])
        destinations += "|" + str(parc['lat']) + "," + str(parc['lng'])

    api_key = "BILLIONS_API_KEY"
    begin = "https://api.nextbillion.io/distancematrix/json?origins="
    end = "&destinations="
    mode = "&mode=car&key="

    url = begin + origins + end + destinations + mode + api_key
    output = requests.get(url).json()
    # Populate matrix with response
    C = []
    for obj in output['rows']:
        row = []
        for data in obj['elements']:
            row.append(data[data_type]['value'])
        row.append(0)
        C.append(row)
    C.append([0] * len(C[0]))
    return C


# Google API cost-matrix
def google(request):
    # Define data type
    if request['vehicles']:
        data_type = 'distance'
    else:
        data_type = 'duration'

    # Generate origin and destination strings for request
    origin = str(request['lat']) + " " + str(request['lng'])
    destinations = str(request['parcels'][0]['lat']) + " " + str(
        request['parcels'][0]['lng'])
    C = []

    for idx, parc in enumerate(request['parcels']):
        if idx > 0:
            destinations += "|" + str(parc['lat']) + " " + str(parc['lng'])

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

    for idx1, start_node in enumerate(request['parcels']):
        origin = str(start_node['lat']) + " " + str(start_node['lng'])
        destinations = str(request['lat']) + " " + str(request['lng'])
        for idx2, parc in enumerate(request['parcels']):
            if idx1 == idx2:
                pass
            else:
                destinations += "|" + str(parc['lat']) + " " + str(parc['lng'])
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
