from utils import recollections as rec

""" optional """
from utils import plot
from utils import generate
import pprint as pp
from data import request_examples as re


def get_recollections_response(req):
    if rec.verify_rec(req) == 1:
        f_request = rec.format_rec(req)
        solution = rec.solve_rec(f_request)
        rsp = rec.get_rec_response(f_request, solution)

        """ optional """
        plt = plot.solution(f_request, solution)
        plt.show()

    else:
        rsp = rec.verify_rec(request)
    return rsp


if __name__ == "__main__":
    # define request
    request = re.req4

    # get response
    response = get_recollections_response(request)

    """ optional """
    pp.pprint(response)
