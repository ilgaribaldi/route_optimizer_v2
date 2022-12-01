from utils import multi_depot as mud
from data import request_examples as re
import pprint as pp
from utils import matrix
from utils import plot


def get_multi_depot_response(req):
    f_request = mud.format_mud(req)
    solution, total_distance = mud.solve_mud(f_request)
    rsp = mud.get_mud_response(f_request, solution, total_distance)

    # optional
    plot.mud_solution(f_request, solution)
    return rsp


if __name__ == "__main__":

    # Define request
    request = re.req7

    response = get_multi_depot_response(request)

    # optional
    pp.pprint(response)



