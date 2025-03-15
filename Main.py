import os
import numpy as np

from src.Extractor import extract_text_from_pdf
from src.Embedder import embed_text
from src.Clusterer import cluster
from src.HTMLGenerator import generate_html

def main():
    # 1. Gather PDFs
    pdf_folder = "data/pdfs"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    # 2. Extract text
    texts = []
    for pdf_file in pdf_files:
        path = os.path.join(pdf_folder, pdf_file)
        text = extract_text_from_pdf(path)
        texts.append((pdf_file, text))

    # 3. Embeddings
    # doc_embedding matches texts (which contains the filename)
    doc_embeddings = []
    for (filename, text) in texts:
        embedding = embed_text(text)
        doc_embeddings.append(embedding)
    doc_embeddings = np.array(doc_embeddings)  # shape: (num_docs, embed_dim)

    # 4. Clustering (K-means as an example)
    clusters = cluster(doc_embeddings)

    # 5. Map cluster IDs to file lists
    cluster_dict = {}
    for idx, cluster_id in enumerate(clusters):
        pdf_file = texts[idx][0]
        if cluster_id not in cluster_dict:
            cluster_dict[cluster_id] = []
        cluster_dict[cluster_id].append(pdf_file)

    # 6. Generate HTML
    generate_html(cluster_dict)


if __name__ == "__main__":
    main()