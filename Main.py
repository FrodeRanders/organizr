import argparse
import os
import sys

from src.Extractor import find_pdfs_recursive
from src.Embedder import extract_and_embed_with_cache
from src.Clusterer import cluster_with_representatives
from src.HTMLGenerator import generate_html

K = 25

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
    embeddings= []
    paths = []

    for pdf_path in pdfs:
        try:
            embedding = extract_and_embed_with_cache(pdf_path)
            if embedding.size > 1:
                embeddings.append(embedding)
                paths.append(pdf_path)
            else:
                print(f"Ignoring bogus embedding: {embedding}")

        except Exception as e:
            print(f"*** [Warning] Could not process '{pdf_path}'. Error: {e}")

    # Clustering
    labels, representatives = cluster_with_representatives(embeddings, paths, K)

    topic_dict = {}
    for idx, label_id in enumerate(labels):
        if label_id not in topic_dict:
            topic_dict[label_id] = []
        topic_dict[label_id].append(paths[idx])

    # Generate HTML
    output_html_path = os.path.join(start_dir, "index.html")
    generate_html(topic_dict, representatives, output_html_path)
    print(f"HTML generated at: {output_html_path}")


if __name__ == "__main__":
    main()