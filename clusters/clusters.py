from k_means_constrained import KMeansConstrained
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans


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
    # Define the maximum cluster size
    max_cluster_size = 100

    # Convert data to numpy array
    data = np.array(list(zip(f_request["lat"], f_request["lng"])))

    # Initialize the MiniBatchKMeans algorithm
    clf = MiniBatchKMeans(
        n_clusters=f_request["clusterAmount"],
        batch_size=1024,
        random_state=0,
        max_iter=3000,
        n_init="auto",
    )

    clf.fit(data)

    # Define a custom predict function that enforces the maximum cluster size constraint
    def custom_predict(clf, X, cluster_sizes):
        # Calculate distances to the cluster centers
        distances = clf.transform(X)
        # Set the distances of clusters with sizes equal to or greater than the max size to infinity
        distances[:, cluster_sizes >= max_cluster_size] = np.inf
        # Return the cluster with the lowest distance
        return np.argmin(distances, axis=1)

    # Initialize an empty array to store the cluster labels
    cls = np.zeros(data.shape[0], dtype=np.int32)

    # Initialize an array to store the cluster sizes
    cluster_sizes = np.zeros(f_request["clusterAmount"], dtype=np.int32)

    # Iterate through each data point and predict the cluster
    for i, point in enumerate(data):
        cluster = custom_predict(clf, point[np.newaxis, :], cluster_sizes)
        cls[i] = cluster
        cluster_sizes[cluster] += 1

    return cls


def get_clusters_with_k_means(f_request):
    # Define the maximum cluster size
    max_cluster_size = 100

    # Convert data to numpy array
    data = np.array(list(zip(f_request["lat"], f_request["lng"])))

    # Initialize the KMeans algorithm
    clf = KMeans(
        n_clusters=f_request["clusterAmount"],
        random_state=3,
        max_iter=100,
        n_init=50000,  # Increase the number of initializations to improve convergence
    )

    clf.fit(data)

    # Define a custom predict function that enforces the maximum cluster size constraint
    def custom_predict(clf, X, cluster_sizes):
        # Calculate distances to the cluster centers
        distances = clf.transform(X)
        # Set the distances of clusters with sizes equal to or greater than the max size to infinity
        distances[:, cluster_sizes >= max_cluster_size] = np.inf
        # Return the cluster with the lowest distance
        return np.argmin(distances, axis=1)

    # Initialize an empty array to store the cluster labels
    cls = np.zeros(data.shape[0], dtype=np.int32)

    # Initialize an array to store the cluster sizes
    cluster_sizes = np.zeros(f_request["clusterAmount"], dtype=np.int32)

    # Iterate through each data point and predict the cluster
    for i, point in enumerate(data):
        cluster = custom_predict(clf, point[np.newaxis, :], cluster_sizes)
        cls[i] = cluster
        cluster_sizes[cluster] += 1

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

