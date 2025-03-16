from sklearn.cluster import KMeans


def cluster(embeddings, num_clusters):
    """
    Cluster embeddings using KMeans, which will try to partition data into 'k' clusters
    """
    num_clusters = min(num_clusters, len(embeddings))

    print(f"Clustering into {num_clusters} clusters...")

    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(embeddings)
    return clusters


# --- ALTERNATIVES ---
#
# Hierarchical clustering:
#     from sklearn.cluster import AgglomerativeClustering
#
#     clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
#     clustering.fit(X)  # X is your array of embeddings
#
# --------------------
#
# Density-based clustering:
#     from sklearn.cluster import DBSCAN
#
#     dbscan = DBSCAN(eps=0.5, min_samples=5)
#     labels = dbscan.fit_predict(X)
#
# Number of clusters is basically determined by how many data points
# get grouped under each label vs. labeled as "noise" (-1).
#

