import argparse
import os
import sys
import numpy as np

from src.Extractor import extract_text_from_pdf, find_pdfs_recursive
from src.Embedder import embed_text
from src.Clusterer import cluster
from src.HTMLGenerator import generate_html



def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Recursively find PDF files, cluster them, and generate an HTML index."
    )
    parser.add_argument(
        "start_dir",
        help="Path to the directory that contains (or has subdirectories containing) PDF files. "
             "Also the directory where the HTML output will be placed."
    )
    args = parser.parse_args()

    # Validate that start_dir is indeed a directory
    start_dir = os.path.abspath(args.start_dir)
    if not os.path.isdir(start_dir):
        print(f"Error: {start_dir} is not a valid directory.")
        sys.exit(1)

    # 1. Gather PDFs
    pdf_files = find_pdfs_recursive(start_dir)
    if not pdf_files:
        print(f"No PDF files found under {start_dir}.")
        sys.exit(0)

    # 2. Extract text
    texts = []
    for path in pdf_files:
        text = extract_text_from_pdf(path)
        texts.append((path, text))

    # 3. Embeddings
    # doc_embedding matches texts (which contains the filename)
    doc_embeddings = []
    for (filename, text) in texts:
        embedding = embed_text(text)
        doc_embeddings.append(embedding)
    doc_embeddings = np.array(doc_embeddings)  # shape: (num_docs, embed_dim)

    # 4. Clustering (K-means as an example)
    clusters = cluster(doc_embeddings, 25)

    # 5. Map cluster IDs to file lists
    cluster_dict = {}
    for idx, cluster_id in enumerate(clusters):
        pdf_file = texts[idx][0]
        if cluster_id not in cluster_dict:
            cluster_dict[cluster_id] = []
        cluster_dict[cluster_id].append(pdf_file)

    # 6. Generate HTML
    output_html_path = os.path.join(start_dir, "index.html")
    generate_html(cluster_dict, output_html_path)
    print(f"HTML generated at: {output_html_path}")


if __name__ == "__main__":
    main()