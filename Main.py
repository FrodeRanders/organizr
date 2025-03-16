import argparse
import os
import sys

from src.Extractor import find_pdfs_recursive
from src.Embedder import extract_and_embed_with_cache
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

    #
    pdfs = find_pdfs_recursive(start_dir)
    if not pdfs:
        print(f"No PDF files found under {start_dir}.")
        sys.exit(0)

    #
    paths = []
    embeddings = []

    for pdf_path in pdfs:
        try:
            embedding = extract_and_embed_with_cache(pdf_path)

            paths.append(pdf_path)
            embeddings.append(embedding)

        except Exception as e:
            print(f"*** [Warning] Could not process '{pdf_path}'. Error: {e}")

    # Clustering
    clusters = cluster(embeddings, 25)

    # Map cluster IDs to file lists
    cluster_dict = {}
    for idx, cluster_id in enumerate(clusters):
        pdf_file = paths[idx]
        if cluster_id not in cluster_dict:
            cluster_dict[cluster_id] = []
        cluster_dict[cluster_id].append(pdf_file)

    # Generate HTML
    output_html_path = os.path.join(start_dir, "index.html")
    generate_html(cluster_dict, output_html_path)
    print(f"HTML generated at: {output_html_path}")


if __name__ == "__main__":
    main()