from dataclasses import dataclass, field
from typing import List

from cachetools import TTLCache

from app.config import settings
from app.schemas import Citation
from app.services.embeddings import Embedder
from app.services.llm import ContextChunk, LLM
from app.services.vector_store import FaissVectorStore

@dataclass
class ChatService:
    store: FaissVectorStore
    embedder: Embedder
    llm: LLM

    # ✅ FIX: use default_factory for mutable defaults
    _cache: TTLCache = field(default_factory=lambda: TTLCache(maxsize=512, ttl=60))

    async def answer(self, question: str) -> tuple[str, List[Citation]]:
        if question in self._cache:
            return self._cache[question]

        q_emb = self.embedder.embed([question])
        results = self.store.search(q_emb, top_k=settings.max_context_chunks)

        context = [ContextChunk(doc_id=m.doc_id, chunk_index=m.chunk_index, text=m.text) for _, m in results]
        answer = await self.llm.answer(question, context)

        citations: List[Citation] = [
            Citation(doc_id=m.doc_id, chunk_index=m.chunk_index, snippet=m.text[:160]) for _, m in results
        ]
        payload = (answer, citations)
        self._cache[question] = payload
        return payload
