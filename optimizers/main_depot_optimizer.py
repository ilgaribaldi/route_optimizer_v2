from utils import main_depot as md

import pprint as pp
from data import request_examples as re

# For testing
from utils import plot
from utils import matrix
from utils import generate


def get_main_depot_response(req):
    if md.verify_md(req) == 1:
        f_request = md.format_md(req)
        solution, total_distance = md.solve_md(f_request)
        rsp = md.get_md_response(f_request, solution, total_distance)
        plt = plot.solution(f_request, solution)
        plt.show()
    else:
        rsp = md.verify_md(req)
    return rsp


if __name__ == "__main__":
    # define initial request
    request = re.req12
    response = get_main_depot_response(request)

    """ optional """
    for obj in response["body"]:
        print(len(obj['route']))

