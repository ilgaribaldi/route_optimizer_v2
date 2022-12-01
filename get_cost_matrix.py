from utils import matrix
import pprint as pp

# Define request
request = {
    "locations": [
        {
            "address": {
                "city": "Ciudad Apodaca",
                "colony": "El Milagro",
                "country": "Mexico",
                "fullName": "Carlos Rousseau 554, El Milagro, Ciudad Apodaca, Nuevo León, Mexico",
                "location": {
                    "coordinates": [
                        -100.1918667,
                        25.7516374
                    ],
                    "type": "Point"
                },
                "postcode": "66634",
                "state": "Nuevo León",
                "street": "Carlos Rousseau"
            },
            "contact": {
                "name": "Bodega Apodaca",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8114119456"
                    }
                ]
            },
            "lat": 25.7516,
            "lng": -100.19186,
            "parcels": [
                {
                    "address": {
                        "city": "Monterrey",
                        "colony": "Centro",
                        "country": "México",
                        "fullName": "Ramón Corona 538, Centro, Monterrey, N.L., México",
                        "location": {
                            "coordinates": [
                                -100.3271996,
                                25.6816308
                            ],
                            "type": "Point"
                        },
                        "postcode": "64000",
                        "state": "Nuevo León",
                        "street": "Ramón Corona"
                    },
                    "contact": {
                        "name": "Alejandro Avila Lopez",
                        "phones": [
                            {
                                "countryCode": "52",
                                "number": "8115550108"
                            }
                        ]
                    },
                    "id": "1",
                    "lat": 25.741077,
                    "lng": -100.35335
                },
                {
                    "address": {
                        "city": "Ciudad General Escobedo",
                        "colony": "Nuevo Escobedo",
                        "country": "México",
                        "fullName": "Alfonso Martínez Domínguez 106, Nuevo Escobedo, Ciudad General Escobedo, N.L., México",
                        "location": {
                            "coordinates": [
                                -100.3761225,
                                25.8001674
                            ],
                            "type": "Point"
                        },
                        "postcode": "66064",
                        "state": "Nuevo León",
                        "street": "Alfonso Martínez Domínguez"
                    },
                    "contact": {
                        "name": "Marina Muñoz",
                        "phones": [
                            {
                                "countryCode": "52",
                                "number": "8130804515"
                            }
                        ]
                    },
                    "id": "2",
                    "lat": 25.74132,
                    "lng": -100.35001
                },
                {
                    "address": {
                        "city": "General Escobedo",
                        "colony": "Brianzzas residencial segundo sector",
                        "country": "Mexico",
                        "fullName": "Calle Tauro 301, 66074 Nuevo Leon, Mexico",
                        "location": {
                            "coordinates": [
                                -100.3403984,
                                25.7927709
                            ],
                            "type": "Point"
                        },
                        "postcode": "66074",
                        "state": "Nuevo León",
                        "street": "Calle Tauro 301"
                    },
                    "contact": {
                        "name": "Maria Alejandra Hernandez",
                        "phones": [
                            {
                                "countryCode": "+52",
                                "number": "81 1749 7798"
                            }
                        ]
                    },
                    "id": "3",
                    "lat": 25.7339,
                    "lng": -100.3492
                },
            ]
        },
        {
            "address": {
                "city": "Monterrey",
                "colony": "Zapata",
                "country": "Mexico",
                "fullName": "Niños Heroes 1205, Zapata, 64390 Monterrey, N.L., Mexico",
                "location": {
                    "coordinates": [
                        -100.3487,
                        25.7591
                    ],
                    "type": "Point"
                },
                "postcode": "64390",
                "state": "Nuevo León",
                "street": "Niños Heroes 1205"
            },
            "contact": {
                "name": "Ellaz",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8181615331"
                    }
                ]
            },
            "lat": 25.743847,
            "lng": -100.355532,
            "parcels": [
                {
                    "address": {
                        "city": "General Escobedo",
                        "colony": "Brianzzas residencial segundo sector",
                        "country": "Mexico",
                        "fullName": "Calle Tauro 301, 66074 Nuevo Leon, Mexico",
                        "location": {
                            "coordinates": [
                                -100.3403984,
                                25.7927709
                            ],
                            "type": "Point"
                        },
                        "postcode": "66074",
                        "state": "Nuevo León",
                        "street": "Calle Tauro 301"
                    },
                    "contact": {
                        "name": "Maria Alejandra Hernandez",
                        "phones": [
                            {
                                "countryCode": "+52",
                                "number": "81 1749 7798"
                            }
                        ]
                    },
                    "id": "4",
                    "lat": 25.732834,
                    "lng": -100.3569
                },
                {
                    "address": {
                        "city": "Santa Catarina",
                        "colony": "Sin Nombre de Colonia 11",
                        "country": "México",
                        "fullName": "Laurel 516, Sin Nombre de Colonia 11, Santa Catarina, N.L., México",
                        "location": {
                            "coordinates": [
                                -100.445918,
                                25.7001848
                            ],
                            "type": "Point"
                        },
                        "postcode": "66360",
                        "state": "Nuevo León",
                        "street": "Laurel"
                    },
                    "contact": {
                        "name": "Alexis Rojas Valdez",
                        "phones": [
                            {
                                "countryCode": "52",
                                "number": "8122038108"
                            }
                        ]
                    },
                    "id": "5",
                    "lat": 25.741997,
                    "lng": -100.35686
                },
                {
                    "address": {
                        "city": "Santa Catarina",
                        "colony": "Sin Nombre de Colonia 11",
                        "country": "México",
                        "fullName": "Laurel 516, Sin Nombre de Colonia 11, Santa Catarina, N.L., México",
                        "location": {
                            "coordinates": [
                                -100.445918,
                                25.7001848
                            ],
                            "type": "Point"
                        },
                        "postcode": "66360",
                        "state": "Nuevo León",
                        "street": "Laurel"
                    },
                    "contact": {
                        "name": "Alexis Rojas Valdez",
                        "phones": [
                            {
                                "countryCode": "52",
                                "number": "8122038108"
                            }
                        ]
                    },
                    "id": "6",
                    "lat": 25.74311,
                    "lng": -100.353459
                },
                {
                    "address": {
                        "city": "General Escobedo",
                        "colony": "Brianzzas residencial segundo sector",
                        "country": "Mexico",
                        "fullName": "Calle Tauro 301, 66074 Nuevo Leon, Mexico",
                        "location": {
                            "coordinates": [
                                -100.3403984,
                                25.7927709
                            ],
                            "type": "Point"
                        },
                        "postcode": "66074",
                        "state": "Nuevo León",
                        "street": "Calle Tauro 301"
                    },
                    "contact": {
                        "name": "Maria Alejandra Hernandez",
                        "phones": [
                            {
                                "countryCode": "+52",
                                "number": "81 1749 7798"
                            }
                        ]
                    },
                    "id": "7",
                    "lat": 25.736,
                    "lng": -100.3492
                }
            ]
        },
    ],
}


if __name__ == "__main__":

    # Multi-Depot
    if 'locations' in request.keys():
        cost_matrix = matrix.multi_depot_haversine(request)
        response = {"status": 200, "cost_matrix": cost_matrix}
    # Not Multi-Depot
    else:
        if request['billions_API'] == 1:
            try:
                cost_matrix = matrix.billions(request)
                response = {"status": 200, "cost_matrix": cost_matrix}
            except KeyError:
                response = {"status"}
        else:
            cost_matrix = matrix.haversine(request)
            response = {"status": 200, "cost_matrix": cost_matrix}

    pp.pprint(response)

