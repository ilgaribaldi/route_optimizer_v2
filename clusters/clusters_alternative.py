from sklearn.cluster import MiniBatchKMeans
from scipy.spatial.distance import cdist
import numpy as np
from utils import generate
import random


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
    def custom_predict(clf, X):
        distances = clf.fit_transform(X)
        sizes = np.bincount(clf.labels_, minlength=clf.n_clusters)
        penalty = np.where(sizes >= max_cluster_size, 100, 0)
        scores = distances + penalty
        print('-----------------')
        print(np.argmin(scores, axis=1))
        return np.argmin(scores, axis=1)

    # Override the predict method with the custom implementation
    clf.predict = lambda X: custom_predict(clf, X)

    # Fit the model and predict the clusters
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

    cluster_lists = [c[str(cluster)] for cluster in range(n_clusters)]
    cls['clusters'] = cluster_lists
    return cls


