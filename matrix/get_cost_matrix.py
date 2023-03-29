from utils import matrix
import pprint as pp

# Define request
req = {
    "lat": 25.7025791,
    "lng": -100.3617855,
    "parcels": [
        {
            "lat": 25.7533112,
            "lng": -100.1563532,
            "id": "64134f934caa528858ba48b8",
            "contact": {
                "name": "Miguel Alberto Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8121898982"
                    }
                ]
            },
            "address": {
                "fullName": "Portal de Santander 422, Portal de Huinala, 66646 Apodaca, Nuevo León, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Portal de Santander",
                "postcode": "66646",
                "colony": "Portal de Huinala",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1563532,
                        25.7533112
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.727917,
            "lng": -100.3570483,
            "id": "64134f934caa528858ba48a7",
            "contact": {
                "name": "Victor Hugo Campos Gutierrez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110607536"
                    }
                ]
            },
            "address": {
                "fullName": "Pico de Aneto 4833, Villa Mitras, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Pico de Aneto 4833",
                "postcode": "64170",
                "colony": "Villa Mitras",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3570483,
                        25.727917
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7284998,
            "lng": -100.1679612,
            "id": "64134f934caa528858ba4889",
            "contact": {
                "name": "Alejandra Hernandez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8130890817"
                    }
                ]
            },
            "address": {
                "fullName": "Nigeria 213, Lomas del Pedregal, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Nigeria 213",
                "postcode": "66648",
                "colony": "Lomas del Pedregal",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1679612,
                        25.7284998
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7914649,
            "lng": -100.2525961,
            "id": "64134f934caa528858ba4898",
            "contact": {
                "name": "Maria Guadalupe Sanchez Rosales ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8186834393"
                    }
                ]
            },
            "address": {
                "fullName": "N15 300, Metroplex II, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "N15 300",
                "postcode": "66612",
                "colony": "Metroplex II",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2525961,
                        25.7914649
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.8000752,
            "lng": -100.43806,
            "id": "64134f934caa528858ba4878",
            "contact": {
                "name": "Luis Brayan Martinez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8132563587"
                    }
                ]
            },
            "address": {
                "fullName": "Moradilla 210, Paraje San José, Parque Industrial Ciudad Mitras, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Parque Industrial Ciudad Mitras",
                "street": "Moradilla 210",
                "postcode": "66023",
                "colony": "Paraje San José",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.43806,
                        25.8000752
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7159447,
            "lng": -100.3773168,
            "id": "64134f934caa528858ba4869",
            "contact": {
                "name": "Oscar Adrian Garcia Oviedo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8186827146"
                    }
                ]
            },
            "address": {
                "fullName": "Paseo de Los Conquistadores 608A, Cumbres 3o. Sector, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Paseo de Los Conquistadores 608a",
                "postcode": "64610",
                "colony": "Cumbres 3o. Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3773168,
                        25.7159447
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7886091,
            "lng": -100.3088226,
            "id": "64134f934caa528858ba4858",
            "contact": {
                "name": "Celia Santillan",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110712761"
                    }
                ]
            },
            "address": {
                "fullName": "De Los Eucaliptos 112, Escobedo Residencial, Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "De Los Eucaliptos 112",
                "postcode": "66057",
                "colony": "Escobedo Residencial",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3088226,
                        25.7886091
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7138891,
            "lng": -100.2222558,
            "id": "6411125bae83e6bedb5f6586",
            "contact": {
                "name": "Valery Cortes",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125684277"
                    }
                ]
            },
            "address": {
                "fullName": "Pintores 222, Blas Chumacero CTM, San Nicolás de los Garza, Nuevo León, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Pintores",
                "postcode": "66473",
                "colony": "Blas Chumacero CTM",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2222558,
                        25.7138891
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7616686,
            "lng": -100.4292595,
            "id": "6411125bae83e6bedb5f6564",
            "contact": {
                "name": "Luis Alberto Olivares",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8114958964"
                    }
                ]
            },
            "address": {
                "fullName": "Lomas de los Encinos 421, Nuevo León, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Mitras Poniente",
                "street": "Lomas de los Encinos 421",
                "postcode": "66024",
                "colony": "Las Lomas sector privadas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4292595,
                        25.7616686
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6919866,
            "lng": -100.2063669,
            "id": "6411125bae83e6bedb5f6553",
            "contact": {
                "name": "Gloria Reyes",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110388601"
                    }
                ]
            },
            "address": {
                "fullName": "Venustiano Carranza 4120, Nuevo San Rafael, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Venustiano Carranza 4120",
                "postcode": "67110",
                "colony": "Nuevo San Rafael",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2063669,
                        25.6919866
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6010156,
            "lng": -100.2692907,
            "id": "640f53e4a4dfbedaa52205ba",
            "contact": {
                "name": "Gabriela Benavides",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116892426"
                    }
                ]
            },
            "address": {
                "fullName": "Plaza de la Mariscala 37, Ciudad Satélite, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Plaza de la Mariscala 37",
                "postcode": "64960",
                "colony": "Ciudad Satélite",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2692907,
                        25.6010156
                    ]
                }
            },
            "volume": 1800
        },
        {
            "lat": 25.7880522,
            "lng": -100.246392,
            "id": "64136742b5549e70bd578dae",
            "contact": {
                "name": "Briza   Flores Cortina",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8991923878"
                    }
                ]
            },
            "address": {
                "fullName": "Hacienda Rioja 730, 66612 Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Hacienda Rioja 730",
                "postcode": "66612",
                "colony": "privada hacienda santa isabel ",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.246392,
                        25.7880522
                    ]
                }
            },
            "volume": 9000
        },
        {
            "lat": 25.6241365,
            "lng": -100.291862,
            "id": "641263210d0f133aebaf097b",
            "contact": {
                "name": "Perla Ayala",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8181690957"
                    }
                ]
            },
            "address": {
                "fullName": "Cerro de Las Mitras 4412, Mirador Residencial, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Cerro de Las Mitras 4412",
                "postcode": "64910",
                "colony": "Mirador Residencial",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.291862,
                        25.6241365
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7366065,
            "lng": -100.2167672,
            "id": "6413448b4caa528858b88b08",
            "contact": {
                "name": "Rodolfo Garza",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8126462894"
                    }
                ]
            },
            "address": {
                "fullName": "San Bernabé 1327, Residencial San Cristobal 3er Sector, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "San Bernabé 1327",
                "postcode": "66478",
                "colony": "Residencial San Cristobal 3er Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2167672,
                        25.7366065
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6445353,
            "lng": -100.1928374,
            "id": "6413448b4caa528858b88b17",
            "contact": {
                "name": "Rodrigo Garza Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8129356023"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Rancho Verde 243, Rancho Viejo, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Calle Rancho Verde 243",
                "postcode": "67192",
                "colony": "Rancho Viejo",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1928374,
                        25.6445353
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7047028,
            "lng": -100.5071602,
            "id": "6413448b4caa528858b88ae8",
            "contact": {
                "name": "CLaudia Rodriguez Buendia",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8119736455"
                    }
                ]
            },
            "address": {
                "fullName": "Hacienda San José 414, Hacienda el Palmar, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Hacienda San José 414",
                "postcode": "66367",
                "colony": "Hacienda el palmar",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5071602,
                        25.7047028
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7093358,
            "lng": -100.2343215,
            "id": "6413448b4caa528858b88af7",
            "contact": {
                "name": "Juan Armando Lopez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8111832322"
                    }
                ]
            },
            "address": {
                "fullName": "Serena Residencial, Nube 715, Sin Nombre de Colonia 46, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Nube 715",
                "postcode": "67129",
                "colony": "Sin Nombre de Colonia 46",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2343215,
                        25.7093358
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7000998,
            "lng": -100.1501999,
            "id": "6413448b4caa528858b88ad9",
            "contact": {
                "name": "Juan de  La Garza",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8129341431"
                    }
                ]
            },
            "address": {
                "fullName": "Andres Quintana Roo 1011, 67130 N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Andres Quintana Roo 1011",
                "postcode": "67130",
                "colony": "Cerradas de Mexico",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1501999,
                        25.7000998
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6611715,
            "lng": -100.4519494,
            "id": "6413448b4caa528858b88ac8",
            "contact": {
                "name": "Zullamyd Camarillo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8126952945"
                    }
                ]
            },
            "address": {
                "fullName": "Bosques de la Huasteca, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Rio de Janeiro 156",
                "postcode": "66354",
                "colony": "Bosques de la Huasteca",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4519494,
                        25.6611715
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6594796,
            "lng": -100.1482355,
            "id": "6413448b4caa528858b88ab7",
            "contact": {
                "name": "Jesus Zuñiga",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8131205717"
                    }
                ]
            },
            "address": {
                "fullName": "China 212, Nuevo León, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "China 212",
                "postcode": "67190",
                "colony": "Nuevo León",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1482355,
                        25.6594796
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7952904,
            "lng": -100.4202425,
            "id": "6413448b4caa528858b88aa6",
            "contact": {
                "name": "Pedro Jean Carlos Navarro Blanco",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8131585832"
                    }
                ]
            },
            "address": {
                "fullName": "San Miguel 239, Villas de San Martín, Parque Industrial Ciudad Mitras, Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "San Miguel 239",
                "postcode": "66005",
                "colony": "Villas de San Martín",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4202425,
                        25.7952904
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.761011,
            "lng": -100.2906954,
            "id": "641072ad13f0658f27c2f524",
            "contact": {
                "name": "Hugo Hugo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8132455483"
                    }
                ]
            },
            "address": {
                "fullName": "Ignacio Aldama 800, Centro, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Ignacio Aldama 800",
                "postcode": "66400",
                "colony": "Centro",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2906954,
                        25.761011
                    ]
                }
            },
            "volume": 3150
        },
        {
            "lat": 25.6327997,
            "lng": -100.279354,
            "id": "641072ad13f0658f27c2f513",
            "contact": {
                "name": "Gerardo Perez Hernandez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112364619"
                    }
                ]
            },
            "address": {
                "fullName": "Aries, Contry, 64860 Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Av Garza Sada 3869 1 ",
                "postcode": "64860",
                "colony": "Contry",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.279354,
                        25.6327997
                    ]
                }
            },
            "volume": 3150
        },
        {
            "lat": 25.72398,
            "lng": -100.34541,
            "id": "64116b407ae22df1ba24c844",
            "contact": {
                "name": "Valeria MontaÃ±o  ",
                "phones": [
                    {
                        "countryCode": "+52",
                        "number": "5.28E+11"
                    }
                ]
            },
            "address": {
                "fullName": "Cuautla 218, Valle Morelos, 64180 Monterrey, NL, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "218 Cuautla",
                "postcode": "64180",
                "colony": "Valle Morelos",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.34541,
                        25.72398
                    ]
                }
            },
            "volume": 6992
        },
        {
            "lat": 25.7225154,
            "lng": -100.2300485,
            "id": "64113be54708b77d0ef2e0a2",
            "contact": {
                "name": "BRANDO JESUS TORRES ALVAREZ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8118777201"
                    }
                ]
            },
            "address": {
                "fullName": "Avenida Rómulo Garza 555, Industrias del Vidrio Oriente, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Avenida Rómulo Garza 555",
                "postcode": "66470",
                "colony": "Industrias del Vidrio",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2300485,
                        25.7225154
                    ]
                }
            },
            "volume": 6000
        },
        {
            "lat": 25.7223551,
            "lng": -100.345338,
            "id": "64124cc0318725b35e9003e7",
            "contact": {
                "name": "Mari Puente",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8134688895"
                    }
                ]
            },
            "address": {
                "fullName": "Amayuca 152, Valle Morelos, 64180 Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "AMayuca 152",
                "postcode": "64180",
                "colony": "Valle Morelos",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.345338,
                        25.7223551
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6748291,
            "lng": -100.2155063,
            "id": "64124cc0318725b35e9003d6",
            "contact": {
                "name": "Perla  Castro",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8118272869"
                    }
                ]
            },
            "address": {
                "fullName": "Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Peñitas 314",
                "postcode": "67189",
                "colony": "Nuevo Almaguer ",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2155063,
                        25.6748291
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.657797,
            "lng": -100.282514,
            "id": "64124cc0318725b35e9003c7",
            "contact": {
                "name": "Mark Estrada ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8661205874"
                    }
                ]
            },
            "address": {
                "fullName": "Avenida Revolución 2000, Plaza Revoluci, Buenos Aires, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Avenida Revolución 2000",
                "postcode": "64800",
                "colony": "Plaza Revoluci",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.282514,
                        25.657797
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7405566,
            "lng": -100.2835168,
            "id": "64124cc0318725b35e9003b8",
            "contact": {
                "name": "Jocelyn Villalon",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116112565"
                    }
                ]
            },
            "address": {
                "fullName": "Girasoles 431, Paseo de las Puentes, 66460 San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Girasoles 431",
                "postcode": "66460",
                "colony": "Paseo de las Puentes",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2835168,
                        25.7405566
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7702283,
            "lng": -100.2581175,
            "id": "640fbee21f54a85bf1f24c84",
            "contact": {
                "name": "Graciela Muñiz Banda",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125142590"
                    }
                ]
            },
            "address": {
                "fullName": "Nogal 221, Los Fresnos I, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Nogal 221",
                "postcode": "66636",
                "colony": "Los Fresnos I",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2581175,
                        25.7702283
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6091645,
            "lng": -100.1820022,
            "id": "64125d0b634400940707ab16",
            "contact": {
                "name": "Eva Guadalupe Hernandez munoz",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8136026811"
                    }
                ]
            },
            "address": {
                "fullName": "Titanes 176, Fraccionamiento Arcadia, Jardines de la Silla, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Jardines de la Silla",
                "street": "Titanes",
                "postcode": "67286",
                "colony": "Fraccionamiento Arcadia",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1820022,
                        25.6091645
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7671139,
            "lng": -100.258559,
            "id": "64125d0b634400940707aaf6",
            "contact": {
                "name": "Silvestre Garcia",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116086868"
                    }
                ]
            },
            "address": {
                "fullName": "Huizache 122, Enramada V, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Huizache 122",
                "postcode": "66635",
                "colony": "Enramada V",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.258559,
                        25.7671139
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7839985,
            "lng": -100.258249,
            "id": "64125d0b634400940707ab05",
            "contact": {
                "name": "Claudia Martinez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8325829613"
                    }
                ]
            },
            "address": {
                "fullName": "Nigeria 750, Prados de La Cieneguita, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Nigeria 750",
                "postcode": "66636",
                "colony": "Prados de La Cieneguita",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.258249,
                        25.7839985
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7059428,
            "lng": -100.2606832,
            "id": "64125d0b634400940707aae5",
            "contact": {
                "name": "Perla  Rangel",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8119928542"
                    }
                ]
            },
            "address": {
                "fullName": "Monte Chimborazo 437, Francisco Garza Sada, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Monte Chimborazo 437",
                "postcode": "66490",
                "colony": "Francisco Garza Sada",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2606832,
                        25.7059428
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7363939,
            "lng": -100.3289798,
            "id": "64125d0b634400940707aad4",
            "contact": {
                "name": "Kevin Jair Diaz Herrera",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8111836273"
                    }
                ]
            },
            "address": {
                "fullName": "Monterrey 6642, Topo Chico, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Monterrey 6642",
                "postcode": "64260",
                "colony": "Topo Chico",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3289798,
                        25.7363939
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7756271,
            "lng": -100.3903364,
            "id": "64125d0b634400940707aac5",
            "contact": {
                "name": "Jose Rafael Lopez Tovar",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8131155628"
                    }
                ]
            },
            "address": {
                "fullName": "Piriápolis 302, Barrio San Luis, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Piriápolis 302",
                "postcode": "64102",
                "colony": "Barrio San Luis",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3903364,
                        25.7756271
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7838585,
            "lng": -100.4338036,
            "id": "64125d0b634400940707aab4",
            "contact": {
                "name": "Miguel Angel Rodriguez Castro",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8180888088"
                    }
                ]
            },
            "address": {
                "fullName": "Pino 625, Mitras Poniente, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Mitras Poniente",
                "street": "Pino 625",
                "postcode": "66023",
                "colony": "Mitras Poniente",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4338036,
                        25.7838585
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6028588,
            "lng": -100.2547869,
            "id": "64125d0b634400940707aaa5",
            "contact": {
                "name": "Mayela Loera",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8180179357"
                    }
                ]
            },
            "address": {
                "fullName": "Fraccionamento Pedregal la Silla Sur 5482, Pedregal La Silla, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Fraccionamento Pedregal la Silla  5482",
                "postcode": "64898",
                "colony": "Pedregal La Silla",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2547869,
                        25.6028588
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6947879,
            "lng": -100.4536289,
            "id": "64125d0b634400940707aa96",
            "contact": {
                "name": "Angel Gutierrez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8120309995"
                    }
                ]
            },
            "address": {
                "fullName": "Calle 11 Poniente 314, Adolfo López Mateos, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Calle 11 Poniente 314",
                "postcode": "66360",
                "colony": "Adolfo López Mateos",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4536289,
                        25.6947879
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6301624,
            "lng": -100.1050822,
            "id": "640f57f8a4dfbedaa5228449",
            "contact": {
                "name": "Damaris Esparza",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8133849533"
                    }
                ]
            },
            "address": {
                "fullName": "Portal del Valle 344, Portal de Juarez, Juárez, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Portal del Valle 344",
                "postcode": "67266",
                "colony": "Portal de Juarez",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1050822,
                        25.6301624
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6364944,
            "lng": -100.298114,
            "id": "641254456344009407049d67",
            "contact": {
                "name": "Alejandro Arroyo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8182709673"
                    }
                ]
            },
            "address": {
                "fullName": "Arturo B. de La Garza 3433, Burócratas Municipales, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Arturo B. de La Garza 3343",
                "postcode": "64769",
                "colony": "Burócratas Municipales",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.298114,
                        25.6364944
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6562348,
            "lng": -100.4541032,
            "id": "641254456344009407049d49",
            "contact": {
                "name": "Jose CARLOS Sada",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112776269"
                    }
                ]
            },
            "address": {
                "fullName": "Las Huastecas, Avenida Miguel Alemán 399, Privadas la Huasteca, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Avenida Miguel Alemán 339",
                "postcode": "66354",
                "colony": "Privadas la Huasteca",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4541032,
                        25.6562348
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6865772,
            "lng": -100.4439899,
            "id": "641254456344009407049d3a",
            "contact": {
                "name": "SOfia Melendez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8182103293"
                    }
                ]
            },
            "address": {
                "fullName": "General Antonio I Villarreal 200, Mártires de Cananea, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "General Antonio I Villarreal 200",
                "postcode": "66365",
                "colony": "Mártires de Cananea",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4439899,
                        25.6865772
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7885279,
            "lng": -100.5788103,
            "id": "641254456344009407049d29",
            "contact": {
                "name": "Yaretzi Monserrat Flores",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8118983339"
                    }
                ]
            },
            "address": {
                "fullName": "Villa Roma 104, Privadas de las Villas, García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Villa Roma 104",
                "postcode": "66000",
                "colony": "Privadas de las Villas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5788103,
                        25.7885279
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6306037,
            "lng": -100.1009305,
            "id": "641254456344009407049d18",
            "contact": {
                "name": "Alexis Alberto  Gonzalez Puente",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125657297"
                    }
                ]
            },
            "address": {
                "fullName": "Fraccionamiento Portal de las Huertas 206, Portal de Juarez, Juárez, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Fraccionamiento Portal de las Huertas 206",
                "postcode": "67266",
                "colony": "Portal de Juarez",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1009305,
                        25.6306037
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.5660599,
            "lng": -100.2736854,
            "id": "641254456344009407049d09",
            "contact": {
                "name": "David Treviño Sanchez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112421209"
                    }
                ]
            },
            "address": {
                "fullName": "Bosque del Paraiso 125, Sierra Alta 90 Sector, Sin Nombre de Colonia 64, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Bosque del Paraiso 125",
                "postcode": "64989",
                "colony": "Sierra Alta 90 Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2736854,
                        25.5660599
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6834165,
            "lng": -100.237648,
            "id": "641254456344009407049cf8",
            "contact": {
                "name": "Barbara Olazaran",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116165202"
                    }
                ]
            },
            "address": {
                "fullName": "Chichimeca 339, Azteca, vista city, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "vista city",
                "street": "Chichimeca 339",
                "postcode": "67150",
                "colony": "Azteca",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.237648,
                        25.6834165
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.664692,
            "lng": -100.4514715,
            "id": "6412ac3e4caa528858b3f79e",
            "contact": {
                "name": "Cristina  Palacios ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "4492637190"
                    }
                ]
            },
            "address": {
                "fullName": "Calle de los cerezos 1062 Santa Catarina Código postal 66376",
                "country": "Mexico",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Cerezos 1062",
                "postcode": "66376",
                "colony": "Santa Catalina",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4514715,
                        25.664692
                    ]
                }
            },
            "volume": 5890
        },
        {
            "lat": 25.7873524,
            "lng": -100.3325,
            "id": "641250244eaa704cfd247f86",
            "contact": {
                "name": "Ruben Alberto Banda Jeronimo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112435613"
                    }
                ]
            },
            "address": {
                "fullName": "Rey Fernando de Aragón 840, Quinto Centenario, Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "Rey Fernando de Aragón 840",
                "postcode": "66072",
                "colony": "Quinto Centenario",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3325,
                        25.7873524
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6622012,
            "lng": -100.414555,
            "id": "641250234eaa704cfd247f77",
            "contact": {
                "name": "Eloit Alan Herrera Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8328578775"
                    }
                ]
            },
            "address": {
                "fullName": "Daniel Dávila 158, Lázaro Garza Ayala, San Pedro Garza García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "Daniel Dávila 158",
                "postcode": "66238",
                "colony": "Lázaro Garza Ayala",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.414555,
                        25.6622012
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6825626,
            "lng": -100.4998325,
            "id": "641250234eaa704cfd247f55",
            "contact": {
                "name": "Erycka Zapata",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8118411504"
                    }
                ]
            },
            "address": {
                "fullName": "Hacienda de Ábregos del Sur 4041, Lomas de Santa Catarina, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Hacienda de Ábregos del Sur 4041",
                "postcode": "66359",
                "colony": "Lomas de Santa Catarina",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4998325,
                        25.6825626
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7840974,
            "lng": -100.3957976,
            "id": "641250234eaa704cfd247f44",
            "contact": {
                "name": "Maria JOsefina Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8121899338"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Parque Tlacota 114, Barrio Del Parque, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Calle Parque Tlacota 114",
                "postcode": "64102",
                "colony": "Barrio Del Parque",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3957976,
                        25.7840974
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6907802,
            "lng": -100.4594008,
            "id": "641250234eaa704cfd247f33",
            "contact": {
                "name": "Carlos Reyes",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8117006528"
                    }
                ]
            },
            "address": {
                "fullName": "San Judas Tadeo 209, Provivienda del Poniente 4to Sector, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "San Judas Tadeo 209",
                "postcode": "66129",
                "colony": "Provivienda del Poniente 4to Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4594008,
                        25.6907802
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6807443,
            "lng": -100.30923,
            "id": "641250234eaa704cfd247f24",
            "contact": {
                "name": "Leticia Guadalupe Vega Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112728201"
                    }
                ]
            },
            "address": {
                "fullName": "Treviño 546, Centro, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Jerónimo Treviño 546",
                "postcode": "64000",
                "colony": "Centro",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.30923,
                        25.6807443
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7277731,
            "lng": -100.3512246,
            "id": "64134cc04caa528858b9ffbe",
            "contact": {
                "name": "Aranza Gallegos",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8119089642"
                    }
                ]
            },
            "address": {
                "fullName": "Alma Mater 3621, Balcones de Aztlán (Residencial Licenciado Raúl Frías), Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Alma Mater 3621",
                "postcode": "64165",
                "colony": "Balcones de Aztlán (Residencial Licenciado Raúl Frías)",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3512246,
                        25.7277731
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6966716,
            "lng": -100.2102579,
            "id": "64134cc04caa528858b9ffcf",
            "contact": {
                "name": "Jorge  Esquivel",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8128791372"
                    }
                ]
            },
            "address": {
                "fullName": "Zafiro 1604, Valle de San Rafael, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Zafiro 1604",
                "postcode": "67118",
                "colony": "Valle de San Rafael",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2102579,
                        25.6966716
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.766009,
            "lng": -100.3740793,
            "id": "64134cc04caa528858b9ffa0",
            "contact": {
                "name": "Jorge Alberto Ramos Olivares",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8114856645"
                    }
                ]
            },
            "address": {
                "fullName": "Oboe 242, San Bernabé IX Sector, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Oboe 242",
                "postcode": "64105",
                "colony": "San Bernabé IX Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3740793,
                        25.766009
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6450868,
            "lng": -100.2072426,
            "id": "64134cc04caa528858b9ffaf",
            "contact": {
                "name": "Martin Martinez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110106499"
                    }
                ]
            },
            "address": {
                "fullName": "Pedro Ramírez 3434, Villa Olímpica, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Pedro Ramírez 3434",
                "postcode": "67180",
                "colony": "Villa Olímpica",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2072426,
                        25.6450868
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.71571,
            "lng": -100.2791652,
            "id": "64134cc04caa528858b9ff8f",
            "contact": {
                "name": "Francisco Vives",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8117164076"
                    }
                ]
            },
            "address": {
                "fullName": "Hong Kong 225, Futuro Nogalar, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Hong Kong 225",
                "postcode": "66484",
                "colony": "Futuro Nogalar",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2791652,
                        25.71571
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7331146,
            "lng": -100.3142932,
            "id": "64134cc04caa528858b9ff80",
            "contact": {
                "name": "Rosalinda Lozano Garza",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8183666650"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Ramón de Campoamor 330, Anáhuac, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Calle Ramón de Campoamor 330",
                "postcode": "66450",
                "colony": "Anáhuac",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3142932,
                        25.7331146
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7316375,
            "lng": -100.3161232,
            "id": "64134cc04caa528858b9ff6f",
            "contact": {
                "name": "Graciela Alvarez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116112047"
                    }
                ]
            },
            "address": {
                "fullName": "Avenida Manuel L. Barragán 6600, Valle de Anáhuac, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Avenida Manuel L. Barragán 6600",
                "postcode": "66450",
                "colony": "Valle de anahuac",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3161232,
                        25.7316375
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6537177,
            "lng": -100.2173803,
            "id": "641203264708b77d0e0089d5",
            "contact": {
                "name": "Clarisa Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125196372"
                    }
                ]
            },
            "address": {
                "fullName": "De Las Mitras 3023, Lomas de San Roque, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "De Las Mitras 3023 ",
                "postcode": "67180",
                "colony": "Lomas de San Roque",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2173803,
                        25.6537177
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7332648,
            "lng": -100.2837696,
            "id": "6413522b4caa528858ba9d1c",
            "contact": {
                "name": "Lizeth ELIZONDO",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112302631"
                    }
                ]
            },
            "address": {
                "fullName": "Calle 23 618, Residencial las Puentes, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Calle 23 618",
                "postcode": "66460",
                "colony": "Residencial las Puentes",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2837696,
                        25.7332648
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6526851,
            "lng": -100.0855507,
            "id": "6413522b4caa528858ba9d0b",
            "contact": {
                "name": "Juan Jose Sosa Guel",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8133820269"
                    }
                ]
            },
            "address": {
                "fullName": "Real de Santa Rosa 313, Real de San José 2 Sector, Juárez, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Real de Santa Rosa 313",
                "postcode": "67250",
                "colony": "Real de San José 2 Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.0855507,
                        25.6526851
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7361882,
            "lng": -100.338025,
            "id": "6413522b4caa528858ba9ceb",
            "contact": {
                "name": "Christian Garcia Galindo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8183014673"
                    }
                ]
            },
            "address": {
                "fullName": "Salinas 2517, Tierra y Libertad Sector Sur, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Salinas 2517",
                "postcode": "64244",
                "colony": "Tierra y Libertad Sector Sur",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.338025,
                        25.7361882
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.8079719,
            "lng": -100.2577123,
            "id": "6413522b4caa528858ba9cfa",
            "contact": {
                "name": "Miguel Alexander Sanchez Cruz",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8182086996"
                    }
                ]
            },
            "address": {
                "fullName": "Av. Adolfo López Mateos 201, Moises Sáenz, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Avenida Adolfo López Mateos 201",
                "postcode": "66613",
                "colony": "Moises Sáenz",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2577123,
                        25.8079719
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7109268,
            "lng": -100.3280531,
            "id": "6413522b4caa528858ba9ccd",
            "contact": {
                "name": "Gregorio Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116310775"
                    }
                ]
            },
            "address": {
                "fullName": "Avenida Bernardo Reyes 3818, Popular, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Avenida Bernardo Reyes 3810",
                "postcode": "64290",
                "colony": "Estrella",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3280531,
                        25.7109268
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6516228,
            "lng": -100.3326298,
            "id": "6413522b4caa528858ba9cbc",
            "contact": {
                "name": "Jesus Cabrera",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8120292797"
                    }
                ]
            },
            "address": {
                "fullName": "9 FUEGOS, Trebol Park, Avenida Lázaro Cárdenas, Residencial San Agustín 1er Sector, San Pedro Garza García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "Avenida Lázaro Cárdenas 2424",
                "postcode": "66260",
                "colony": "Residencial San Agustín 1er Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3326298,
                        25.6516228
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7292123,
            "lng": -100.1570753,
            "id": "6413522b4caa528858ba9cab",
            "contact": {
                "name": "Daniel Ivan Bustos",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8115099017"
                    }
                ]
            },
            "address": {
                "fullName": "J. Vizcarra 446, Misión Real, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "José Vizcarra 446",
                "postcode": "66640",
                "colony": "Misión Real",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1570753,
                        25.7292123
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6076899,
            "lng": -100.1681717,
            "id": "6411f7e3cea59a02a112b596",
            "contact": {
                "name": "Amparo Elizabeth Esquivel Bonilla ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8134410534"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Alebrije, Colonia Rehiletes, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Calle Alebrije 688",
                "postcode": "67286",
                "colony": "Colonia Rehiletes",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1681717,
                        25.6076899
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6847475,
            "lng": -100.4216909,
            "id": "6411f7e3cea59a02a112b587",
            "contact": {
                "name": "Valeria Navarro",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8333090445"
                    }
                ]
            },
            "address": {
                "fullName": "Palenque 330, Fama II, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Palenque 330",
                "postcode": "66116",
                "colony": "Fama II",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4216909,
                        25.6847475
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6585468,
            "lng": -100.4127852,
            "id": "64123d130d0f133aeb79035b",
            "contact": {
                "name": "VIRGINIA REYES GONZALEZ",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8111656993"
                    }
                ]
            },
            "address": {
                "fullName": "Los Sauces 816, Los Sauces 2o Sector, 66237 San Pedro Garza García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "Los Sauces 816",
                "postcode": "66237",
                "colony": "Los Sauces 2o Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4127852,
                        25.6585468
                    ]
                }
            },
            "volume": 75
        },
        {
            "lat": 25.7003885,
            "lng": -100.5044076,
            "id": "641116a8ae83e6bedb600759",
            "contact": {
                "name": "Pedro Castro",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8115283863"
                    }
                ]
            },
            "address": {
                "fullName": "Rio San Pedro 183, Bosques de la Huasteca, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Rio San Pedro 183",
                "postcode": "66367",
                "colony": "Bosques la huasteca ",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5044076,
                        25.7003885
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6956435,
            "lng": -100.2826482,
            "id": "6411d1c6f55bc231407ae1df",
            "contact": {
                "name": "Jose Rocha",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8120002574"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Peral 2614a, Moderna, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Calle Peral 2614A",
                "postcode": "64530",
                "colony": "Moderna",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2826482,
                        25.6956435
                    ]
                }
            },
            "volume": 3150
        },
        {
            "lat": 25.6638206,
            "lng": -100.1204308,
            "id": "6411d1c6f55bc231407ae1bd",
            "contact": {
                "name": "Janeth Macias",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8114691997"
                    }
                ]
            },
            "address": {
                "fullName": "Begonia 501, Paseo Las Margaritas, Juárez, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Begonia 501",
                "postcode": "67280",
                "colony": "Paseo Las Margaritas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1204308,
                        25.6638206
                    ]
                }
            },
            "volume": 3150
        },
        {
            "lat": 25.7790789,
            "lng": -100.2652704,
            "id": "6411d1c6f55bc231407ae19b",
            "contact": {
                "name": "Gerardo Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110440259"
                    }
                ]
            },
            "address": {
                "fullName": "Paseo de Las Palmas ÌII, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Henequen 550 ",
                "postcode": "66635",
                "colony": "Paseo de Las Palmas ÌII",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2652704,
                        25.7790789
                    ]
                }
            },
            "volume": 3150
        },
        {
            "lat": 25.7261256,
            "lng": -100.1544714,
            "id": "64125739a9efe7286ebc6a09",
            "contact": {
                "name": "Pablo Hernandez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8341113466"
                    }
                ]
            },
            "address": {
                "fullName": "Degas 513, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Degas 513",
                "postcode": "66644",
                "colony": "Mision Real ",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1544714,
                        25.7261256
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7998002,
            "lng": -100.5763101,
            "id": "64125739a9efe7286ebc69fa",
            "contact": {
                "name": "Miguel Alonso",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8121987246"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Estaño 137, Paseo de las Minas, García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Calle Estaño 137",
                "postcode": "66000",
                "colony": "Paseo de las Minas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5763101,
                        25.7998002
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7999982,
            "lng": -100.4798924,
            "id": "64125739a9efe7286ebc69e9",
            "contact": {
                "name": "Jose de Jesus Mota Garcia",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8123728116"
                    }
                ]
            },
            "address": {
                "fullName": "Valle del Paraguay 613, Valle de Lincoln, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Valle del Paraguay 613",
                "postcode": "66026",
                "colony": "Valle de Lincoln",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4798924,
                        25.7999982
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7753872,
            "lng": -100.2532515,
            "id": "64125739a9efe7286ebc69da",
            "contact": {
                "name": "Eduardo Rafael Juarez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8123909292"
                    }
                ]
            },
            "address": {
                "fullName": "Hacienda Guadalupe 306, Los Pinos IV, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Hacienda Guadalupe 306",
                "postcode": "66636",
                "colony": "Magnolias",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2532515,
                        25.7753872
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6807077,
            "lng": -100.3083822,
            "id": "64125739a9efe7286ebc69c9",
            "contact": {
                "name": "Alejandro Damian  Arellano Mireles",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8188000591"
                    }
                ]
            },
            "address": {
                "fullName": "Jerónimo Treviño 624, Centro, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Jerónimo Treviño 624",
                "postcode": "64000",
                "colony": "Centro",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3083822,
                        25.6807077
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6528362,
            "lng": -100.0767105,
            "id": "64125739a9efe7286ebc69b8",
            "contact": {
                "name": "Giovanni Aguilar",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8181123959"
                    }
                ]
            },
            "address": {
                "fullName": "Clavel 313, Villas de San Juan, Colinas de San Juan(Colinas de La Morena), Juárez, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Juárez",
                "street": "Avenida Paseo de San Juan 313",
                "postcode": "67254",
                "colony": "Colinas de San Juan(Colinas de La Morena)",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.0767105,
                        25.6528362
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7768014,
            "lng": -100.3152685,
            "id": "64125739a9efe7286ebc69a7",
            "contact": {
                "name": "Jose de Jesus Cantu",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8130384411"
                    }
                ]
            },
            "address": {
                "fullName": "Vía Antonio Pisano 423, Joyas de Anáhuac Sector Florencia, Joyas de Anahuac, Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "Vía Antonio Pisano 423",
                "postcode": "66055",
                "colony": "Joyas de Anáhuac Sector Florencia",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3152685,
                        25.7768014
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6746058,
            "lng": -100.4423188,
            "id": "64125a204bc9e5cf5f6c170a",
            "contact": {
                "name": "Yamileth Garcia",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110153291"
                    }
                ]
            },
            "address": {
                "fullName": "Tulipán 434, Jardines de Santa Catarina ÌII, Jardines de Santa Catarina III, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Tulipan 434",
                "postcode": "66376",
                "colony": "Jardines de Snata Catarina ",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4423188,
                        25.6746058
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.765065,
            "lng": -100.2651374,
            "id": "64125a204bc9e5cf5f6c16f9",
            "contact": {
                "name": "Alondra Yaretzy Hernandez Cuellar",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8128654624"
                    }
                ]
            },
            "address": {
                "fullName": "Elisa Garza, Mujeres Ilustres (Fomerrey 4), Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Elisa Garza 404",
                "postcode": "66635",
                "colony": "Mujeres Ilustres (Fomerrey 4)",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2651374,
                        25.765065
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6503994,
            "lng": -100.1818257,
            "id": "64125a204bc9e5cf5f6c16ea",
            "contact": {
                "name": "Mario Gonzalez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "81103389081"
                    }
                ]
            },
            "address": {
                "fullName": "Jardines de Gibraltar, Jardines de Andalucía, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Jardines de Gibraltar 7829",
                "postcode": "67193",
                "colony": "Jardines de Andalucía",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1818257,
                        25.6503994
                    ]
                }
            },
            "volume": 11
        },
        {
            "lat": 25.7553587,
            "lng": -100.1898515,
            "id": "64125a204bc9e5cf5f6c16d9",
            "contact": {
                "name": "Ana gabriela De Leon Sarmiento",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8115713348"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Martel 511, Milimex, 66637 Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Calle Martel 511",
                "postcode": "66637",
                "colony": "Milimex",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1898515,
                        25.7553587
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7678288,
            "lng": -100.3789709,
            "id": "641262388f6364cbd363f0bd",
            "contact": {
                "name": "Maggy Gonzalez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116668912"
                    }
                ]
            },
            "address": {
                "fullName": "Canalera 449, San Bernabé XI Sector, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Canalera 449",
                "postcode": "64105",
                "colony": "San Bernabé XI Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3789709,
                        25.7678288
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6412533,
            "lng": -100.1846727,
            "id": "641262388f6364cbd363f0ac",
            "contact": {
                "name": "Jose Miguel Escobedo Alvarez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8124205046"
                    }
                ]
            },
            "address": {
                "fullName": "Yahualica 144, Tierra Propia 1er Sector, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Yahualica 144",
                "postcode": "67190",
                "colony": "Tierra Propia 1er Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1846727,
                        25.6412533
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6466135,
            "lng": -100.1741165,
            "id": "641262388f6364cbd363f09b",
            "contact": {
                "name": "Braulio Torres",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8116030691"
                    }
                ]
            },
            "address": {
                "fullName": "Transporte Aéreo 7622, S.c.t., Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Transporte Aéreo 7622",
                "postcode": "67199",
                "colony": "S.c.t.",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1741165,
                        25.6466135
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7786771,
            "lng": -100.4690641,
            "id": "641262388f6364cbd363f08c",
            "contact": {
                "name": "Yadira Rodriguez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8181179957"
                    }
                ]
            },
            "address": {
                "fullName": "Jardines Helenos 124, Veranda, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Jardines Helenos 124",
                "postcode": "66036",
                "colony": "Veranda",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4690641,
                        25.7786771
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7994424,
            "lng": -100.575576,
            "id": "641262388f6364cbd363f07b",
            "contact": {
                "name": "yuri Alfaro",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8112365880"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Cobre 142, Paseo de las Minas, 66003 García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Calle Cobre 142",
                "postcode": "66003",
                "colony": "Paseo de las Minas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.575576,
                        25.7994424
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6717093,
            "lng": -100.4660833,
            "id": "641262388f6364cbd363f06a",
            "contact": {
                "name": "Neftali Gamez Aguilar",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8113119715"
                    }
                ]
            },
            "address": {
                "fullName": "1A Avenida 252, Santa Martha I, 66350 Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "1A Avenida 252",
                "postcode": "66350",
                "colony": "Ixtlera",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4660833,
                        25.6717093
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.8035104,
            "lng": -100.3482877,
            "id": "641262388f6364cbd363f059",
            "contact": {
                "name": "Karen de  Luna",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110656261"
                    }
                ]
            },
            "address": {
                "fullName": "Siderúrgica 116, Parque Industrial Escobedo, Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "Siderúrgica 116",
                "postcode": "66062",
                "colony": "Parque Industrial Escobedo",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3482877,
                        25.8035104
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7726842,
            "lng": -100.4106086,
            "id": "6413411bd3358b3a478d73eb",
            "contact": {
                "name": "Alexis Arzola",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8113921903"
                    }
                ]
            },
            "address": {
                "fullName": "Cantantes 506, La Alianza, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Cantantes 506",
                "postcode": "64103",
                "colony": "La alianza",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4106086,
                        25.7726842
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6921432,
            "lng": -100.4372871,
            "id": "6413411bd3358b3a478d73fc",
            "contact": {
                "name": "Luis Angel Espinoza Orozco",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8123831529"
                    }
                ]
            },
            "address": {
                "fullName": "Cataluña 343, Prados del Rey, Santa Catarina, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Santa Catarina",
                "street": "Cataluña 343",
                "postcode": "66365",
                "colony": "Prados del Rey",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4372871,
                        25.6921432
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7391772,
            "lng": -100.2751188,
            "id": "6413411bd3358b3a478d73da",
            "contact": {
                "name": "Irving Trinidad",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8661547526"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Cerro de Pasco 859, Balcones de las Puentes, San Nicolás de los Garza, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Calle Cerro de Pasco 859",
                "postcode": "66466",
                "colony": "Balcones de las Puentes",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2751188,
                        25.7391772
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7996401,
            "lng": -100.5795261,
            "id": "6413411bd3358b3a478d73c9",
            "contact": {
                "name": "Victor Hugo Reyes Martinez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125772771"
                    }
                ]
            },
            "address": {
                "fullName": "Titanio 204, Paseo de las Minas, García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Titanio 204",
                "postcode": "66000",
                "colony": "Paseo de las Minas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5795261,
                        25.7996401
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7294405,
            "lng": -100.4002187,
            "id": "6413411bd3358b3a478d73ba",
            "contact": {
                "name": "Christian Torres",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110158280"
                    }
                ]
            },
            "address": {
                "fullName": "Coruña 245, Bosques de Las Cumbres, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Coruña 245",
                "postcode": "64619",
                "colony": "Bosques de Las Cumbres",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4002187,
                        25.7294405
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.8027075,
            "lng": -100.5780167,
            "id": "6413411bd3358b3a478d739c",
            "contact": {
                "name": "ALejandro Castillo",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8117598208"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Paladio 252, Paseo de las Minas, García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Calle Paladio 252",
                "postcode": "66003",
                "colony": "Paseo de las minas",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.5780167,
                        25.8027075
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7412596,
            "lng": -100.1851503,
            "id": "6413411bd3358b3a478d73ab",
            "contact": {
                "name": "Maria Medina",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8126465879"
                    }
                ]
            },
            "address": {
                "fullName": "Residencial Joyas de Huinala, Antiguo Camino A. Huinala, Valle de Huinala IV, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Antiguo Camino A. Huinala 117",
                "postcode": "66633",
                "colony": "Valle de Huinala IV",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1851503,
                        25.7412596
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.681623,
            "lng": -100.1736132,
            "id": "6413411bd3358b3a478d738d",
            "contact": {
                "name": "Marco Antonio Ramirez Cortez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8131918305"
                    }
                ]
            },
            "address": {
                "fullName": "Calle Río Amazonas 1820, Dos Ríos Sector XII, Guadalupe, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Guadalupe",
                "street": "Calle Río Amazonas 1820",
                "postcode": "67196",
                "colony": "Dos Ríos Sector XII",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1736132,
                        25.681623
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7796217,
            "lng": -100.4285502,
            "id": "641348d74caa528858b97d12",
            "contact": {
                "name": "Israel Valdez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8124160022"
                    }
                ]
            },
            "address": {
                "fullName": "Sierra la Laguna 937, Mitras Poniente, Villas del Poniente, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Villas del Poniente",
                "street": "Sierra la Laguna 937",
                "postcode": "66023",
                "colony": "Mitras Poniente",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4285502,
                        25.7796217
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7076049,
            "lng": -100.1490781,
            "id": "641348d74caa528858b97d01",
            "contact": {
                "name": "Joel David Ruiz Chavez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8141438398"
                    }
                ]
            },
            "address": {
                "fullName": "Fuentes de San miguel, Fuente de Cantera, Misión de San Miguel, Ciudad Apodaca, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad Apodaca",
                "street": "Fuente de Cantera 118",
                "postcode": "66647",
                "colony": "Misión de San Miguel",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.1490781,
                        25.7076049
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7919654,
            "lng": -100.4959429,
            "id": "641348d74caa528858b97cf0",
            "contact": {
                "name": "Diego Ivan Moreno Najera",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8123464398"
                    }
                ]
            },
            "address": {
                "fullName": "Granate 317, Valle de Lincoln, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "García",
                "street": "Granate 317",
                "postcode": "66026",
                "colony": "Valle de Lincoln",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.4959429,
                        25.7919654
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.7945619,
            "lng": -100.3449394,
            "id": "641348d74caa528858b97cd0",
            "contact": {
                "name": "Luis Gerardo Garcia",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8125949317"
                    }
                ]
            },
            "address": {
                "fullName": "Palermo 132, Mirasur, 66070 Ciudad General Escobedo, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Ciudad General Escobedo",
                "street": "Palermo 132",
                "postcode": "66070",
                "colony": "Mirasur",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3449394,
                        25.7945619
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6287876,
            "lng": -100.3052514,
            "id": "641348d74caa528858b97cdf",
            "contact": {
                "name": "Jorge Morales",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8128992091"
                    }
                ]
            },
            "address": {
                "fullName": "Mauritania 4432, Laderas del Mirador (Fomerrey 21), Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Mauritania 4432",
                "postcode": "64765",
                "colony": "Laderas del Mirador (Fomerrey 21)",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3052514,
                        25.6287876
                    ]
                }
            },
            "volume": 11
        },
        {
            "lat": 25.6081994,
            "lng": -100.2680966,
            "id": "641348d74caa528858b97cbf",
            "contact": {
                "name": "Miguel Vega",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8123265923"
                    }
                ]
            },
            "address": {
                "fullName": "Avenida Eugenio Garza Sada 6115, Villa Las Fuentes, Monterrey, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Avenida Eugenio Garza Sada 6115",
                "postcode": "64890",
                "colony": "Villa Las Fuentes",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2680966,
                        25.6081994
                    ]
                }
            },
            "volume": 1
        },
        {
            "lat": 25.6226741,
            "lng": -100.3063005,
            "id": "641367afb5549e70bd579a80",
            "contact": {
                "name": "ALEJANDRA TAPIA",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8119903812"
                    }
                ]
            },
            "address": {
                "fullName": "Priv. San Antonio 5618, Colonia Miguel Hidalgo, Monterrey, Nuevo Leon, Mexico",
                "country": "Mexico",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "Privada San Antonio 5618",
                "postcode": "64926",
                "colony": "Colonia Miguel Hidalgo",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3063005,
                        25.6226741
                    ]
                }
            },
            "volume": 3230
        },
        {
            "lat": 25.6592604,
            "lng": -100.3961377,
            "id": "6410bf19bc368dccd9a62834",
            "contact": {
                "name": "Fernanda Gomez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8130822730"
                    }
                ]
            },
            "address": {
                "fullName": "Lazaro Garza Ayala 973, Casco Urbano, 66230 San Pedro Garza García, N.L., México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "Lazaro Garza Ayala 973",
                "postcode": "66230",
                "colony": "Casco Urbano",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3961377,
                        25.6592604
                    ]
                }
            },
            "volume": 4400
        },
        {
            "lat": 25.6382076,
            "lng": -100.3897971,
            "id": "641363db31f8cd12495687fc",
            "contact": {
                "name": "DANIELA CALDERON GIL",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8119093885"
                    }
                ]
            },
            "address": {
                "fullName": "Pedregal del Valle, 66280 San Pedro Garza García, Nuevo Leon, Mexico",
                "country": "Mexico",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "Amatista 120 casa 1",
                "postcode": "66280",
                "colony": "Pedregal del Valle",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3897971,
                        25.6382076
                    ]
                }
            },
            "volume": 3230
        },
        {
            "lat": 25.7161085,
            "lng": -100.2175007,
            "id": "641363db31f8cd12495687ed",
            "contact": {
                "name": "FLOR ESTEFANIA SANTIAGO",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8110093879"
                    }
                ]
            },
            "address": {
                "fullName": "Calle de los Aperos 603, Villa de San Miguel la Talaverna, San Nicolás de los Garza, Nuevo Leon, Mexico",
                "country": "Mexico",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Calle de los Aperos 603",
                "postcode": "66473",
                "colony": "Villa de San Miguel la Talaverna",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2175007,
                        25.7161085
                    ]
                }
            },
            "volume": 3230
        },
        {
            "lat": 25.64855,
            "lng": -100.3824,
            "id": "6411fb014708b77d0efddd10",
            "contact": {
                "name": "Paola Martinez",
                "phones": [
                    {
                        "countryCode": "+52",
                        "number": "81 1181 9446"
                    }
                ]
            },
            "address": {
                "fullName": "Pedro Moya 100c, Capistrano, 66244 San Pedro Garza García, NL, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "San Pedro Garza García",
                "street": "100c Pedro Moya",
                "postcode": "66244",
                "colony": "Capistrano",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.3824,
                        25.64855
                    ]
                }
            },
            "volume": 4400
        },
        {
            "lat": 25.69486,
            "lng": -100.35431,
            "id": "6411fb014708b77d0efddd1f",
            "contact": {
                "name": "Andrea Martinez Guerra",
                "phones": [
                    {
                        "countryCode": "+52",
                        "number": "8114189498"
                    }
                ]
            },
            "address": {
                "fullName": "Francisco Fernández Treviño 482, Leones, 64600 Monterrey, NL, México",
                "country": "México",
                "state": "Nuevo León",
                "city": "Monterrey",
                "street": "482 Francisco Fernández Treviño",
                "postcode": "64600",
                "colony": "Leones",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.35431,
                        25.69486
                    ]
                }
            },
            "volume": 4400
        },
        {
            "lat": 25.732714,
            "lng": -100.2728311,
            "id": "64128c246d322166951ff1b2",
            "contact": {
                "name": "Carlos Gonzalez",
                "phones": [
                    {
                        "countryCode": "52",
                        "number": "8114836643"
                    }
                ]
            },
            "address": {
                "fullName": "C. 10 299, Jardines de Anahuac 2do Sector, San Nicolás de los Garza, Nuevo Leon, Mexico",
                "country": "Mexico",
                "state": "Nuevo León",
                "city": "San Nicolás de los Garza",
                "street": "Calle 10",
                "postcode": "66463",
                "colony": "Jardines de Anahuac 2do Sector",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -100.2728311,
                        25.732714
                    ]
                }
            },
            "volume": 2500
        }
    ],
    "billions_API": 0
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
