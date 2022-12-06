from utils import on_demand as od

""" optional """
from utils import generate
from utils import plot
import pprint as pp
from data import request_examples as re


def get_on_demand_response(req):
    if od.verify_od(req) == 1:
        f_request = od.format_od(req)
        solution = od.solve_od(f_request)
        rsp = od.get_od_response(f_request, solution)
    else:
        rsp = od.verify_od(request)
    return rsp


if __name__ == "__main__":
    # define request
    request = re.req3

    # get response
    response = get_on_demand_response(request)
    pp.pprint(response)

    """ optional """
    pp.pprint(response)
    plt = plot.response(response)
    plt.show()

