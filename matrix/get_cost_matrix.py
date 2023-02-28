from utils import matrix
import pprint as pp

# Define request
req = {
    "vehicleMaxVolume": [
        10,
        9,
        8
    ],
    "vehicles": 2,
    "end_locations": [],
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
    "parcels": [
        {
            "id": "1",
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
            },
            "volume": 1
        },
        {
            "id": "2",
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
            },
            "volume": 1
        },
    ],
    "billions_API": 0,
    "search_strategy": 1,
    "cost_matrix": [
        [0.0,
         755.8980673113974,
         575.158699922519,
         372.8848755351363,
         321.7438299248847,
         373.37097077682137,
         181.8812357415378,
         445.34495615136547,
         494.20266495466666,
         777.2862538562285,
         830.6180047134467,
         0],
        [755.8980673113974,
         0.0,
         518.7193833322657,
         391.5593266305651,
         685.0044270547065,
         769.8213220523573,
         766.7366569815679,
         1200.135687344938,
         1178.0428237933024,
         949.5168304880672,
         1410.2339033138044,
         0],
        [575.158699922519,
         518.7193833322657,
         0.0,
         340.99164013654655,
         300.80793208870784,
         341.87009040551754,
         705.5869524608494,
         932.4683018118352,
         800.9104665174513,
         1174.3842727515373,
         1399.141292956751,
         0],
        [372.8848755351363,
         391.5593266305651,
         340.99164013654655,
         0.0,
         330.2602244480944,
         423.36732923452365,
         429.8026327552807,
         812.2793940717594,
         791.2022028162463,
         834.1375038504945,
         1122.8350208467389,
         0],
        [321.7438299248847,
         685.0044270547065,
         300.80793208870784,
         330.2602244480944,
         0.0,
         93.58038400798188,
         489.3715364402936,
         632.0497521369446,
         515.1800148388986,
         1048.405891350747,
         1148.554032048969,
         0],
        [373.37097077682137,
         769.8213220523573,
         341.87009040551754,
         423.36732923452365,
         93.58038400798188,
         0.0,
         550.7631290661828,
         614.9849609588923,
         459.071635518257,
         1125.6912623192059,
         1182.7622628729885,
         0],
        [181.8812357415378,
         766.7366569815679,
         705.5869524608494,
         429.8026327552807,
         489.3715364402936,
         550.7631290661828,
         0.0,
         505.46894831340785,
         633.2545738244244,
         599.0201476411546,
         698.3728854504091,
         0],
        [445.34495615136547,
         1200.135687344938,
         932.4683018118352,
         812.2793940717594,
         632.0497521369446,
         614.9849609588923,
         505.46894831340785,
         0.0,
         285.777860688527,
         1011.463913533071,
         717.5714133842779,
         0],
        [494.20266495466666,
         1178.0428237933024,
         800.9104665174513,
         791.2022028162463,
         515.1800148388986,
         459.071635518257,
         633.2545738244244,
         285.777860688527,
         0.0,
         1210.7913705146668,
         1000.1343316913548,
         0],
        [777.2862538562285,
         949.5168304880672,
         1174.3842727515373,
         834.1375038504945,
         1048.405891350747,
         1125.6912623192059,
         599.0201476411546,
         1011.463913533071,
         1210.7913705146668,
         0.0,
         667.0803686266588,
         0],
        [830.6180047134467,
         1410.2339033138044,
         1399.141292956751,
         1122.8350208467389,
         1148.554032048969,
         1182.7622628729885,
         698.3728854504091,
         717.5714133842779,
         1000.1343316913548,
         667.0803686266588,
         0.0,
         0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
}


def get_matrix(request):
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

    return response


if __name__ == "__main__":
    rsp = get_matrix(req)

    # optional
    pp.pprint(rsp)
