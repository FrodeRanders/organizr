import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans



def pick_representative_doc(centroid_vec, cluster_embeddings):
    """
    Given a centroid (1D vector) and a set of document embeddings (2D array),
    returns the index of the doc with the highest cosine similarity to the centroid.
    """
    centroid_vec_2d = centroid_vec.reshape(1, -1)  # shape (1, embed_dim)
    similarities = cosine_similarity(centroid_vec_2d, cluster_embeddings)[0]  # shape (num_docs_in_cluster,)
    best_idx = np.argmax(similarities)
    return best_idx, similarities[best_idx]


def cluster_with_representatives(embeddings, doc_filenames, k):
    """
    Cluster embeddings using KMeans into 'k' clusters. Returns:
      - labels: an array of cluster IDs (same order as 'embeddings'),
      - representatives: a list of "best doc path" for each cluster.
    """
    # If we request more clusters than documents, reduce k
    k = min(k, len(embeddings))

    # Fit K-Means
    kmeans = KMeans(n_clusters=k, n_init="auto")
    labels = kmeans.fit_predict(embeddings)
    assert len(labels) == len(doc_filenames)


    # For each labeled cluster, pick a representative doc
    np_embeddings = np.array(embeddings)
    representatives = []
    for cluster_id in range(k):
        # 'cluster_indices' is an array of integers, which are indices of the
        # embeddings/documents in this particular cluster
        cluster_indices = np.where(labels == cluster_id)[0]
        if len(cluster_indices) == 0:
            # No documents in this cluster (edge case if KMeans had an empty cluster)
            representatives.append(None)
            continue

        # Grab centroid vector
        centroid_vec = kmeans.cluster_centers_[cluster_id]  # shape (embedding_dim,)

        # 'np_embeddings[cluster_indices]' picks out the corresponding rows (embeddings) for
        # those documents in 'cluster_indices'
        cluster_emb = np_embeddings[cluster_indices]  # shape (n_cluster_docs, embedding_dim)

        # Pick the doc that is closest to the centroid (highest cosine similarity)
        best_idx_in_cluster, best_sim = pick_representative_doc(centroid_vec, cluster_emb)
        global_doc_index = cluster_indices[best_idx_in_cluster]

        # E.g., get the corresponding filename
        rep_path = doc_filenames[global_doc_index]
        representatives.append(rep_path)

    return labels, representatives


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
