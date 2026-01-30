from dataclasses import dataclass
from typing import List

import httpx

from app.config import settings
from app.services.chunking import chunk_text
from app.services.embeddings import Embedder
from app.services.vector_store import ChunkMeta, FaissVectorStore

@dataclass
class IngestService:
    store: FaissVectorStore
    embedder: Embedder

    def ingest_text(self, doc_id: str, text: str) -> int:
        chunks = chunk_text(text)
        embeddings = self.embedder.embed(chunks)
        metas: List[ChunkMeta] = [ChunkMeta(doc_id=doc_id, chunk_index=i, text=ch) for i, ch in enumerate(chunks)]
        self.store.add(embeddings, metas)
        return len(chunks)

    async def ingest_url(self, doc_id: str, url: str) -> int:
        timeout = httpx.Timeout(settings.request_timeout_seconds)
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            r = await client.get(url)
            r.raise_for_status()
            text = r.text
        return self.ingest_text(doc_id, text)
