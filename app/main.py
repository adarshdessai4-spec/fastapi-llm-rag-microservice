from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.correlation_id import CorrelationIdMiddleware
from app.routers import health, ingest, chat, admin

app = FastAPI(title="FastAPI LLM-RAG Microservice", version="1.0.0")

app.add_middleware(CorrelationIdMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(ingest.router, prefix="/v1/ingest", tags=["ingest"])
app.include_router(chat.router, prefix="/v1/chat", tags=["chat"])
app.include_router(admin.router, prefix="/v1/admin", tags=["admin"])
