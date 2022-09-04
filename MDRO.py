from utils import main_depot as md
from utils import generate

from utils import plot
import pprint as pp


def get_main_depot_response(req):
    if md.verify_md(req) == 1:
        f_request = md.format_md(req)
        solution = md.solve_md(f_request)
        rsp = md.get_md_response(f_request, solution)

    else:
        rsp = md.verify_md(req)
    return rsp


if __name__ == "__main__":
    # define request
    request = generate.md_request(25, 2, ['depot', 'depot'])

    # get response
    response = get_main_depot_response(request)

    """ optional """
    # pp.pprint(response)
    # plt = plot.response(response)
    # plt.show()
