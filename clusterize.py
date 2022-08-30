from utils import clusters as cl
from utils import main_depot as md
from utils import plot
from utils import generate
import pprint as pp


def clusterize(req):
    if md.verify_md(req):
        f_request = md.format_md(req)
        n_clusters = 3
        clusters = cl.get_clusters(f_request, n_clusters)
        rsp = cl.get_cluster_response(f_request, clusters)
        plt = plot.clusters(f_request, clusters)
        return rsp, plt
    else:
        rsp = md.verify_md(req)
        return rsp, None


if __name__ == '__main__':
    # define request
    request = generate.md_request(300, 4)

    # get response
    response, plot = clusterize(request)

    """ optional """
    # pp.pprint(response)
    # plot.show()

