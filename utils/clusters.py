from k_means_constrained import KMeansConstrained


# get clusters
def get_clusters(f_req, cluster_number):
    data = list(zip(f_req['lat'][1:], f_req['lng'][1:]))
    clf = KMeansConstrained(
        n_clusters=cluster_number,
        size_min=None,
        size_max=100,
        random_state=0,
        n_jobs=12
    )
    cls = clf.fit_predict(data)
    return cls


# get cluster response
def get_cluster_response(f_req, req_clusters):
    cls = {'Status': 'OK', 'clusters': 0}
    n_clusters = req_clusters.max() + 1
    c = {}
    for cluster in range(n_clusters):
        c[str(cluster)] = []

    for idx, cls_number in enumerate(req_clusters):
        node_info = {
            'contact': f_req['contact'][idx + 1],
            'address': f_req['address'][idx + 1],
            'id': f_req['parcel_id'][idx],
            'lat': f_req['lat'][idx + 1],
            'lng': f_req['lng'][idx + 1]
        }
        c[str(cls_number)].append(node_info)

    cluster_lists = [None] * n_clusters
    for cluster in range(n_clusters):
        cluster_lists[cluster] = c[str(cluster)]
    cls['clusters'] = cluster_lists
    return cls
