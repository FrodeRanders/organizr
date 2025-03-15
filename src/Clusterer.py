from sklearn.cluster import KMeans

NUM_CLUSTERS = 5

def cluster(embeddings):
    num_clusters = min(NUM_CLUSTERS, len(embeddings))

    print(f"Clustering into {num_clusters} clusters...")

    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(embeddings)
    return clusters
