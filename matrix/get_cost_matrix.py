from utils import matrix
import pprint as pp

# Define request
req = {
    "lat": 25.7327,
    "lng": -100.2791,
    "contact": {
        "name": "MAIN DEPOT",
        "phones": [
            {
                "countryCode": "52",
                "number": "8124744958"
            }
        ]
    },
    "address": {
        "fullName": "MAIN DEPOT",
        "country": "-",
        "city": "-",
        "state": "-",
        "street": "-",
        "postcode": "-",
        "colony": "-",
        "location": {
            "type": "-",
            "coordinates": [
                "-100.2791",
                "25.7327"
            ]
        }
    },
    "depots": [
        {
            "id": "1",
            "parcels": ["1.1", "1.2", "1.3"],
            "lat": 25.7952254181278,
            "lng": -100.249475973778,
            "contact": {
                "name": "1",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "1",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.249475973778",
                        "25.7952254181278"
                    ]
                }
            }
        },
        {
            "id": "2",
            "parcels": ["2.1", "2.2"],
            "lat": 25.7812518794152,
            "lng": -100.298906308739,
            "contact": {
                "name": "2",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "2",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.298906308739",
                        "25.7812518794152"
                    ]
                }
            }
        },
        {
            "id": "3",
            "parcels": ["3.1", "3.2"],
            "lat": 25.7651932279431,
            "lng": -100.269895102615,
            "contact": {
                "name": "3",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "3",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.269895102615",
                        "25.7651932279431"
                    ]
                }
            }
        },
        {
            "id": "4",
            "parcels": ["4.1", "4.2"],
            "lat": 25.7542400828131,
            "lng": -100.300548879908,
            "contact": {
                "name": "4",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "4",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.300548879908",
                        "25.7542400828131"
                    ]
                }
            }
        },
        {
            "id": "5",
            "parcels": ["5.1", "5.2"],
            "lat": 25.7520449594731,
            "lng": -100.309569402615,
            "contact": {
                "name": "5",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "5",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.309569402615",
                        "25.7520449594731"
                    ]
                }
            }
        },
        {
            "id": "6",
            "parcels": ["6.1", "6.2"],
            "lat": 25.7272,
            "lng": -100.2620,
            "contact": {
                "name": "6",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "6",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.2620",
                        "25.7272"
                    ]
                }
            }
        },
        {
            "id": "7",
            "parcels": ["7.1"],
            "lat": 25.6974,
            "lng": -100.3001,
            "contact": {
                "name": "7",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "7",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.3001",
                        "25.6974"
                    ]
                }
            }
        },
        {
            "id": "8",
            "parcels": ["8.1"],
            "lat": 25.7126,
            "lng": -100.3231,
            "contact": {
                "name": "8",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "8",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.3231",
                        "25.7126"
                    ]
                }
            }
        },
        {
            "id": "9",
            "parcels": ["9.1"],
            "lat": 25.7210,
            "lng": -100.2026,
            "contact": {
                "name": "9",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "9",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.2026",
                        "25.7210"
                    ]
                }
            }
        },
        {
            "id": "10",
            "parcels": ["10.1", "10.2"],
            "lat": 25.6690,
            "lng": -100.2358,
            "contact": {
                "name": "10",
                "phones": [
                    {
                        "countryCode": "-",
                        "number": "-"
                    }
                ]
            },
            "address": {
                "fullName": "10",
                "country": "-",
                "city": "-",
                "state": "-",
                "street": "-",
                "postcode": "-",
                "colony": "-",
                "location": {
                    "type": "-",
                    "coordinates": [
                        "-100.2358",
                        "25.6690"
                    ]
                }
            }
        }
    ],
    "method": "haversine",
    "search_strategy": 1,
}


def get_matrix(request):
    # Multi-Depot
    if 'locations' in request.keys():
        cost_matrix = matrix.multi_depot_haversine(request)
        response = {"status": 200, "cost_matrix": cost_matrix}

    # Not Multi-Depot
    else:
        if 'billions_API' in request.keys() and request['billions_API'] == 1:
            try:
                cost_matrix = matrix.billions(request)
                response = {"status": 200, "cost_matrix": cost_matrix}
            except KeyError:
                response = {"status": 400}
        else:
            cost_matrix = matrix.haversine(request)
            response = {"status": 200, "cost_matrix": cost_matrix}

    return response


if __name__ == "__main__":
    rsp = get_matrix(req)

    # optional
    pp.pprint(rsp)
