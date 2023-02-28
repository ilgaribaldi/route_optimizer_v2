from k_means_constrained import KMeansConstrained


def format_cluster_request(request):
    return {
        "lat": [parcel['lat'] for parcel in request['parcels']],
        "lng": [parcel['lng'] for parcel in request['parcels']],
        "contact": [parcel['contact'] for parcel in request['parcels']],
        "address": [parcel['address'] for parcel in request['parcels']],
        "parcel_id": [parcel['id'] for parcel in request['parcels']],
        "parcel_volume": [parcel['volume'] for parcel in request['parcels']],
        "clusterAmount": request["clusterAmount"]
    }


def get_clusters(f_request):
    data = list(zip(f_request["lat"], f_request["lng"]))
    clf = KMeansConstrained(
        n_clusters=f_request["clusterAmount"],
        size_min=None,
        size_max=100,
        random_state=0,
        n_jobs=12
    )
    cls = clf.fit_predict(data)
    return cls


def format_cluster_response(f_request, clusters):
    cls = {'status': 200, 'clusters': 0}
    n_clusters = clusters.max() + 1
    c = {}
    for cluster in range(n_clusters):
        c[str(cluster)] = []

    for idx, cls_number in enumerate(clusters):
        node_info = {
            'contact': f_request["contact"][idx],
            'address': f_request['address'][idx],
            'id': f_request['parcel_id'][idx],
            'lat': f_request['lat'][idx],
            'lng': f_request['lng'][idx],
            'volume': f_request["parcel_volume"][idx]
        }
        c[str(cls_number)].append(node_info)

    cluster_lists = [None] * n_clusters
    for cluster in range(n_clusters):
        cluster_lists[cluster] = c[str(cluster)]
    cls['clusters'] = cluster_lists
    return cls

