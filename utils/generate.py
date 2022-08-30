import numpy as np

# generate main depot request
def md_request(deliveries, vehicles, end_locations=None):
    if not end_locations:
        end_locations = []
    np.random.seed(7)
    generated_request = {
        "vehicles": vehicles,
        "end_locations": end_locations,
        "capacities": 28,
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
        }
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

