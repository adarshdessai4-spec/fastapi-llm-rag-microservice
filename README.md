# FastAPI LLM-RAG Microservice

A production-minded **Python/FastAPI** backend service that demonstrates:
- **REST APIs** + clean layering (routers/services/schemas)
- **RAG** (document ingestion → embeddings → vector search → grounded answers)
- **LLM integration** (pluggable provider: OpenAI / local stub)
- **Performance & reliability** basics (async I/O, caching, rate limiting, timeouts)
- **Observability** (structured logs + request correlation ID)
- **Docker + CI** (GitHub Actions) + tests

> Designed as a portfolio repo for Backend Engineer roles (Python | AI/LLM).

## Quickstart (Local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open docs: http://127.0.0.1:8000/docs

## Quickstart (Docker)

```bash
docker build -t rag-fastapi .
docker run --rm -p 8000:8000 rag-fastapi
```

## Env
Copy `.env.example` → `.env`.

## Core APIs
- GET `/health`
- POST `/v1/ingest/text`
- POST `/v1/ingest/url`
- POST `/v1/chat/answer`
- GET `/v1/admin/stats`

## Tests
```bash
pytest -q
```
