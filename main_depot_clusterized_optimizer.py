from utils import main_depot as md
from utils import generate
from utils import plot
import clusterize as clu
import main_depot_optimizer as mdro
import concurrent.futures
import time
import pprint as pp


if __name__ == "__main__":
    start = time.perf_counter()
    request = generate.md_request(300, 3)
    if md.verify_md(request):
        cluster_response, plt = clu.clusterize(request)

        multi_requests = []
        for cluster in cluster_response['clusters']:
            request = {
                "vehicles": 4,
                "end_locations": [],
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
                },
                "parcels": cluster
            }
            multi_requests.append(request)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(mdro.get_main_depot_response, req) for req in multi_requests]
            for f in concurrent.futures.as_completed(results):
                plt = plot.response(f.result())
        plt.show()
    else:
        response = md.verify_md(request)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
