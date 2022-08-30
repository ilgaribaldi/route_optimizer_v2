from utils import on_demand as od
from utils import generate
from utils import plot


def get_on_demand_response(req):
    if od.verify_od(req) == 1:
        f_request = od.format_od(req)
        solution = od.solve_od(f_request)
        rsp = od.get_od_response(f_request, solution)

        """ optional """
        """
        try:
            # plt = plot.solution(f_request, solution)
            # plt.show()
        except NameError:
            # print('plot not available')
        """

    else:
        rsp = od.verify_od(request)
    return rsp


if __name__ == "__main__":
    # define request
    request = generate.od_request(10)

    # get response
    response = get_on_demand_response(request)

