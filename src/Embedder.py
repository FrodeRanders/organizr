from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding
