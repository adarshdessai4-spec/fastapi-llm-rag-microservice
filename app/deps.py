from functools import lru_cache

from app.services.embeddings import Embedder
from app.services.vector_store import FaissVectorStore
from app.services.llm import get_llm
from app.services.ingest_service import IngestService
from app.services.chat_service import ChatService
from app.services.rate_limit import SimpleRateLimiter

@lru_cache
def get_store() -> FaissVectorStore:
    return FaissVectorStore()

@lru_cache
def get_embedder() -> Embedder:
    return Embedder()

@lru_cache
def get_ingest_service() -> IngestService:
    return IngestService(store=get_store(), embedder=get_embedder())

@lru_cache
def get_chat_service() -> ChatService:
    return ChatService(store=get_store(), embedder=get_embedder(), llm=get_llm())

@lru_cache
def get_rate_limiter() -> SimpleRateLimiter:
    return SimpleRateLimiter()
