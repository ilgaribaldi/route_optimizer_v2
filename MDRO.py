from utils import main_depot as md
from utils import plot
from utils import generate


def get_response(req):
    if md.verify(req) == 1:
        f_request = md.rformat(req)
        solution = md.solve(f_request)
        rsp = md.get_response(f_request, solution)
        """ optional """
        # plt = plot.response(rsp)
        # plt.show()
    else:
        rsp = md.verify(req)
    return rsp


if __name__ == "__main__":
    # define request
    request = generate.md_request(50, 2)

    # get response
    response = get_response(request)

    