from sklearn.cluster import KMeans

def cluster(embeddings, num_clusters):
    num_clusters = min(num_clusters, len(embeddings))

    print(f"Clustering into {num_clusters} clusters...")

    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(embeddings)
    return clusters
