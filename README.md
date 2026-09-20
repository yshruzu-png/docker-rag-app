# Dockerized RAG Application

RAG app using Azure OpenAI and Azure AI Search, containerized with Docker.

## Setup
1. Copy `.env.example` to `.env` and fill in your Azure values.
2. Build: `docker build -t rag-app .`
3. Run: `docker run --env-file .env -p 8000:8000 rag-app`

Scripts: `create_index.py` (create the search index), `upload_documents.py` (load documents), `check_indexes.py` (verify).
