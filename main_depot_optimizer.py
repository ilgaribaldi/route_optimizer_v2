from utils import main_depot as md
from utils import plot
import pprint as pp
from data import request_examples as re

# For testing
from utils import matrix
from utils import generate


def get_main_depot_response(req):
    if md.verify_md(req) == 1:
        f_request = md.format_md(req)
        solution, total_distance = md.solve_md(f_request)
        rsp = md.get_md_response(f_request, solution, total_distance)
    else:
        rsp = md.verify_md(req)
    return rsp


if __name__ == "__main__":
    # define initial request
    request = re.req6

    response = get_main_depot_response(request)

    """ optional """
    pp.pprint(response)
    if response['status'] == 200:
        plt = plot.response(response)
        plt.show()
