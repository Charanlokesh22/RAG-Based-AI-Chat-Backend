 RAG-Based AI Chat Backend

A backend service that enables conversational question answering over documents using Retrieval-Augmented Generation (RAG).

 Features
- Document-aware AI chat
- Vector search using FAISS
- LLM-based response generation
- FastAPI backend
- Dockerized deployment

Tech Stack
- Python, FastAPI
- OpenAI API
- FAISS
- PostgreSQL (metadata storage)
- Docker

Architecture
1. User query is converted to embedding
2. Relevant document chunks retrieved via vector search
3. Retrieved context injected into LLM prompt
4. LLM generates grounded response

 Setup
```bash
git clone https://github.com/yourname/rag-ai-chat-backend
cd rag-ai-chat-backend
docker build -t rag-chat .
docker run -p 8000:8000 rag-chat
