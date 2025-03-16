from os import path, makedirs
import numpy as np
import hashlib
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

EMBEDDINGS_CACHE_DIR = "./embedding-cache"
makedirs(EMBEDDINGS_CACHE_DIR, exist_ok=True)

def SHA1(path: str) -> str:
    return hashlib.sha1(path.encode("utf-8")).hexdigest()

def get_embedding_cache_path(pdf_path):
    """
    Compute a hash of the absolute file path (or the file contents)
    and create a filename in the EMBEDDINGS_CACHE_DIR.
    """
    abs_path = path.abspath(pdf_path)

    # Hash of filename
    path_hash = SHA1(abs_path)
    cache_filename = f"{path_hash}.npy"
    return path.join(EMBEDDINGS_CACHE_DIR, cache_filename)


def embed_text(text):
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding


def embed_text_with_cache(pdf_path, text):
    """
    If the embedding for this PDF has been computed before, load from disk.
    Otherwise, compute the embedding and save it to cache.
    """
    makedirs(EMBEDDINGS_CACHE_DIR, exist_ok=True)
    name = path.basename(pdf_path)

    cache_path = get_embedding_cache_path(pdf_path)

    if path.exists(cache_path):
        # Load the cached embedding
        print(f"Cached embedding: {name}")
        embedding = np.load(cache_path)
    else:
        print(f"Embedding: {name}")
        embedding = model.encode(text, convert_to_numpy=True)
        np.save(cache_path, embedding)

    return embedding


class PdfReaderContext:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self._file_handle = None
        self.reader = None

    def __enter__(self):
        self._file_handle = open(self.pdf_path, "rb")
        self.reader = PdfReader(self._file_handle)
        return self.reader

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file_handle.close()


def extract_and_embed_with_cache(pdf_path):
    """
    If the embedding for this PDF has been computed before, load from disk.
    Otherwise, compute the embedding and save it to cache.
    For each page, extract text, embed it, and store embeddings in a list.
    """
    name = path.basename(pdf_path)

    embedding = []

    cache_path = get_embedding_cache_path(pdf_path)
    if path.isfile(cache_path):
        print(f"Loading cached embedding: {name}")
        embedding = np.load(cache_path)
    else:
        print(f"Embedding: {path.basename(cache_path)} <- {name}")
        with PdfReaderContext(pdf_path) as reader:
            if reader is not None:
                page_embeddings = []
                for page_num, page in enumerate(reader.pages):
                    page_text = page.extract_text()
                    if page_text.strip():
                        page_embeddings.append(model.encode(page_text, convert_to_numpy=True))

                embedding = np.mean(page_embeddings, axis=0)
                np.save(cache_path, embedding)

    return embedding
