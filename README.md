FastAPI LLM-RAG Microservice

A production-grade Python backend service demonstrating how to design, build, and deploy
LLM-powered APIs using FastAPI with real-world engineering practices.

This project focuses on productionizing AI systems — not just calling an LLM, but building
backend services that are reliable, observable, scalable, and safe.

🚀 What this project demonstrates

✅ Clean FastAPI architecture (routers / services / schemas / dependencies)
✅ RESTful API design with validation and versioning
✅ Retrieval-Augmented Generation (RAG)
✅ Vector search using FAISS
✅ Pluggable LLM layer (OpenAI or local stub)
✅ Grounded responses with citations
✅ Rate limiting and caching
✅ Async I/O and performance awareness
✅ Correlation IDs for observability
✅ Dockerized deployment
✅ CI pipeline with automated tests

Built as a portfolio-grade backend system for Senior Backend / Backend Engineer III (Python | AI/LLM) roles.

🎯 Why this project exists

Most AI demos stop at simply sending a prompt to an LLM.

In real backend systems, teams must handle:

hallucinations and unreliable responses

performance bottlenecks

API cost control

safe usage of external context

debugging and observability

reproducible deployments

This project demonstrates how LLM systems are actually built in production, not just how they are queried.

🧠 High-Level Architecture
Client
  │
  ▼
FastAPI API Layer
  │
  ├── Request validation (Pydantic)
  ├── Rate limiting
  ├── Correlation IDs
  │
  ├── Ingestion Service
  │       ├── Text / URL ingestion
  │       ├── Chunking
  │       ├── Embedding generation
  │       └── FAISS vector store
  │
  └── Chat Service
          ├── Semantic retrieval (top-k)
          ├── Prompt orchestration
          ├── LLM execution
          └── Grounded response + citations

⚙️ Tech Stack

Language: Python 3.11+

Framework: FastAPI

Validation: Pydantic v2

Vector Database: FAISS

LLM: OpenAI (optional) / Local stub

Async HTTP: httpx

Caching: TTL cache

CI: GitHub Actions

Containerization: Docker

🚀 Quickstart (Local)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs


Health check:

http://127.0.0.1:8000/health

⚡ Demo (30 seconds)
1️⃣ Ingest a document
curl -X POST http://127.0.0.1:8000/v1/ingest/text \
  -H "Content-Type: application/json" \
  -d '{"doc_id":"doc1","text":"FastAPI is a modern Python web framework for building APIs. It supports type hints, Pydantic validation, and automatic OpenAPI documentation."}'

2️⃣ Ask a question (RAG)
curl -X POST http://127.0.0.1:8000/v1/chat/answer \
  -H "Content-Type: application/json" \
  -d '{"question":"What is FastAPI?"}'

Response includes

AI-generated answer

source citations from retrieved context

grounded output to reduce hallucination

🔌 Core APIs
Method	Endpoint	Description
GET	/health	Service health
POST	/v1/ingest/text	Ingest raw text
POST	/v1/ingest/url	Ingest webpage
POST	/v1/chat/answer	RAG-based question answering
GET	/v1/admin/stats	Vector index statistics
🔐 Reliability & Safety

Per-IP request rate limiting

External call timeouts

LLM context isolation

“I don’t know” fallback when context is missing

Citation-based grounding to reduce hallucinations

🧠 Engineering Decisions

RAG instead of raw prompting to reduce hallucination

FAISS chosen for fast local vector search

Pluggable LLM interface to avoid vendor lock-in

Stub LLM for local/offline development

Service layer separation for clean architecture

Async I/O for I/O-bound workloads

Correlation IDs for request tracing and debugging

🐳 Docker
docker build -t fastapi-llm-rag .
docker run -p 8000:8000 fastapi-llm-rag

🧪 Tests
pytest -q


Includes:

health endpoint test

ingestion + chat integration test

✅ What this project demonstrates

End-to-end backend ownership

Strong Python engineering fundamentals

Real-world LLM system design

Production-first mindset

Clean, scalable FastAPI architecture

This mirrors how AI-enabled backend systems are built in real production environments.

👤 Author

Adarsh Dessai
Senior Python Backend Engineer
Focus: FastAPI • Distributed Systems • AI / LLM Integration

✅ Final command
git add README.md
git commit -m "Finalize production-grade README"
git push