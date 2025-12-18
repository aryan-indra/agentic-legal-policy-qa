from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True)

def embed_query(query):
    return model.encode([query])
