import faiss
import numpy as np

index = faiss.IndexFlatL2(1536)
documents = []

def add_embedding(embedding, text):
    index.add(np.array([embedding]).astype("float32"))
    documents.append(text)

def search(query_embedding, top_k=3):
    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )
    return [documents[i] for i in indices[0]]
