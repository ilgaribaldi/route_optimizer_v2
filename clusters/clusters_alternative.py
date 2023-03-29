from sklearn.cluster import MiniBatchKMeans
import numpy as np
from sklearn.cluster import KMeans
from k_means_constrained import KMeansConstrained


def custom_predict(clf, X, cluster_sizes, cluster_sum_distances):
    max_cluster_size = 100
    distances = clf.transform(X)
    avg_distances = np.divide(
        cluster_sum_distances,
        cluster_sizes,
        out=np.zeros_like(cluster_sum_distances),
        where=cluster_sizes != 0
    )
    distances[:, cluster_sizes >= max_cluster_size] = np.inf
    penalty = 0.05
    distances += penalty * avg_distances
    cluster = np.argmin(distances, axis=1)[0]
    return cluster, distances[0, cluster]


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


def get_clusters_with_mini_batch(f_request):
    data = np.array(list(zip(f_request["lat"], f_request["lng"])))

    clf = MiniBatchKMeans(
        n_clusters=f_request["clusterAmount"],
        batch_size=1024,
        random_state=0,
        max_iter=3000,
        n_init="auto",
    )

    clf.fit(data)

    cls = np.zeros(data.shape[0], dtype=np.int32)
    cluster_sizes = np.zeros(f_request["clusterAmount"], dtype=np.int32)
    cluster_sum_distances = np.zeros(f_request["clusterAmount"], dtype=np.float64)

    for i, point in enumerate(data):
        cluster, distance = custom_predict(
            clf,
            point[np.newaxis, :],
            cluster_sizes,
            cluster_sum_distances
        )
        cls[i] = cluster
        cluster_sizes[cluster] += 1
        cluster_sum_distances[cluster] += distance

    return cls


def get_clusters_with_k_means(f_request):
    data = np.array(list(zip(f_request["lat"], f_request["lng"])))

    clf = KMeans(
        n_clusters=f_request["clusterAmount"],
        random_state=3,
        max_iter=10000,
        n_init=500,  # Increase the number of initializations to improve convergence
    )

    clf.fit(data)
    cls = np.zeros(data.shape[0], dtype=np.int32)
    cluster_sizes = np.zeros(f_request["clusterAmount"], dtype=np.int32)
    cluster_sum_distances = np.zeros(f_request["clusterAmount"], dtype=np.float64)

    for i, point in enumerate(data):
        cluster, distance = custom_predict(
            clf,
            point[np.newaxis, :],
            cluster_sizes,
            cluster_sum_distances
        )
        cls[i] = cluster
        cluster_sizes[cluster] += 1
        cluster_sum_distances[cluster] += distance

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

    cluster_lists = [c[str(cluster)] for cluster in range(n_clusters)]
    cls['clusters'] = cluster_lists
    return cls


