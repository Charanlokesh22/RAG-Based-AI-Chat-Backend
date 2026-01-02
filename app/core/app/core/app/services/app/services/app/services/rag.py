from app.services.embeddings import get_embedding
from app.services.vector_store import search
from app.core.llm import generate_answer

def rag_query(question: str):
    query_embedding = get_embedding(question)
    contexts = search(query_embedding)
    combined_context = "\n".join(contexts)
    return generate_answer(combined_context, question)
