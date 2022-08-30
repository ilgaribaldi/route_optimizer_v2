from utils import main_depot as md
from utils import generate
from utils import plot


def get_response(req):
    if md.verify_md(req) == 1:
        f_request = md.format_md(req)
        solution = md.solve_md(f_request)
        rsp = md.get_md_response(f_request, solution)

        """ optional """
        # plt = plot.response(rsp)
        # plt.show()

    else:
        rsp = md.verify_md(req)
    return rsp


if __name__ == "__main__":
    # define request
    request = generate.md_request(100, 4)

    # get response
    response = get_response(request)

    