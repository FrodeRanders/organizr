from sklearn.cluster import KMeans


def cluster(embeddings, k):
    """
    Cluster embeddings using KMeans, which will try to partition data into 'k' clusters
    """
    k = min(k, len(embeddings))

    print(f"Clustering into {k} clusters...")

    kmeans = KMeans(n_clusters=k)
    return kmeans.fit_predict(embeddings)


# --- ALTERNATIVES ---
#
# Hierarchical clustering:
#     from sklearn.cluster import AgglomerativeClustering
#
#     clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
#     clustering.fit(embeddings)
#
# --------------------
#
# Density-based clustering:
#     from sklearn.cluster import DBSCAN
#
#     dbscan = DBSCAN(eps=0.5, min_samples=5)
#     labels = dbscan.fit_predict(embeddings)
#
# Number of clusters is basically determined by how many data points
# get grouped under each label vs. labeled as "noise" (-1).
#

