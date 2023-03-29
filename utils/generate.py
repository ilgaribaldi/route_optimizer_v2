import numpy as np


def cluster_request(deliveries, clusterAmount):
    np.random.seed(7)
    parcels = []
    generated_request = {}

    lat_mean = (25.6672391977154 + 25.7960000000000) / 2
    lng_mean = (-100.368106407827 + (-100.200000000000)) / 2
    lat_std = 0.025  # Adjust this value to control the spread
    lng_std = 0.025  # Adjust this value to control the spread

    for idx in range(deliveries):
        lat = np.random.normal(lat_mean, lat_std)
        lng = np.random.normal(lng_mean, lng_std)

        # Clip lat and lng values to be within the specified range
        lat = np.clip(lat, 25.6672391977154, 25.7960000000000)
        lng = np.clip(lng, -100.368106407827, -100.200000000000)
        parcel_info = {
            "id": str(idx + 1),
            "lat": lat,
            "lng": lng,
            "contact": {
                "name": str(idx + 1),
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": str(idx + 1),
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        str(lat),
                        str(lng)
                    ]
                }
            },
            "volume": np.random.uniform(1, 10)
        }
        parcels.append(parcel_info)

    generated_request['parcels'] = parcels
    generated_request['clusterAmount'] = clusterAmount
    return generated_request


# generate on demand request
def od_request(deliveries):
    np.random.seed(7)
    generated_request = {
        "lat": 25.7327,
        "lng": -100.2791,
        "contact": {
            "name": "client1",
            "phones": [
                {
                    "countryCode": "52",
                    "number": "8124744958"
                }
            ]
        },
        "address": {
            "fullName": "client1",
            "country": "-",
            "city": "-",
            "state": "-",
            "street": "-",
            "postcode": "-",
            "colony": "-",
            "location": {
                "type": "-",
                "coordinates": [
                    "25.7327",
                    "-100.2791"
                ]
            }
        },
        "api": "billions",
    }
    parcels = []
    for idx in range(deliveries):
        lat = np.random.uniform(25.6672391977154, 25.7960000000000)
        lng = np.random.uniform(-100.368106407827, -100.200000000000)
        parcel_info = {
            "id": str(idx + 1),
            "lat": lat,
            "lng": lng,
            "contact": {
                "name": str(idx + 1),
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": str(idx + 1),
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        str(lat),
                        str(lng)
                    ]
                }
            }
        }
        parcels.append(parcel_info)

    generated_request['parcels'] = parcels
    return generated_request

