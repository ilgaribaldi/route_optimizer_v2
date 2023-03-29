from utils import plot
from utils import generate
import pprint as pp
# import clusters as cl
import clusters_alternative as cl


def get_cluster_response(request):
    f_request = cl.format_cluster_request(request)
    clusters = cl.get_clusters_with_k_means(f_request)
    rsp = cl.format_cluster_response(f_request, clusters)
    plt = plot.clusters(f_request, clusters)
    plt.show()
    return rsp


if __name__ == '__main__':
    # define request
    req = generate.cluster_request(399, 4)

    # get response
    response = get_cluster_response(req)

    for obj in response["clusters"]:
        print(len(obj))

    # print response
    pp.pprint(response)

