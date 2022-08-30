from utils import clusters as cl
from utils import main_depot as md
from utils import plot
from utils import generate
import pprint as pp


def get_clusters(req):
    if md.verify(req):
        f_request = md.rformat(req)
        n_clusters = 2
        clusters = cl.clusterize(f_request, n_clusters)
        rsp = cl.get_response(f_request, clusters)
        plt = plot.clusters(f_request, clusters)
        return rsp, plt
    else:
        rsp = md.verify(req)
        return rsp, None


if __name__ == '__main__':
    print('-----')
    request = generate.md_request(300, 4)
    response, plot = get_clusters(request)
    pp.pprint(response)
    plot.show()

