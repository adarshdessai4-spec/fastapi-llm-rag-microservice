import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import faiss
import numpy as np

DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))
INDEX_PATH = DATA_DIR / "faiss.index"
META_PATH = DATA_DIR / "meta.npy"

@dataclass
class ChunkMeta:
    doc_id: str
    chunk_index: int
    text: str

class FaissVectorStore:
    def __init__(self, dim: int = 384):
        self.dim = dim
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.index = faiss.IndexFlatIP(dim)
        self.metas: List[ChunkMeta] = []
        self._load_if_exists()

    def _load_if_exists(self) -> None:
        if INDEX_PATH.exists() and META_PATH.exists():
            self.index = faiss.read_index(str(INDEX_PATH))
            raw = np.load(str(META_PATH), allow_pickle=True).tolist()
            self.metas = [ChunkMeta(**m) for m in raw]

    def _persist(self) -> None:
        faiss.write_index(self.index, str(INDEX_PATH))
        np.save(str(META_PATH), np.array([m.__dict__ for m in self.metas], dtype=object), allow_pickle=True)

    def add(self, embeddings: np.ndarray, metas: List[ChunkMeta]) -> None:
        assert embeddings.shape[1] == self.dim
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings.astype("float32"))
        self.metas.extend(metas)
        self._persist()

    def search(self, query_embedding: np.ndarray, top_k: int) -> List[Tuple[float, ChunkMeta]]:
        faiss.normalize_L2(query_embedding)
        scores, idxs = self.index.search(query_embedding.astype("float32"), top_k)
        out: List[Tuple[float, ChunkMeta]] = []
        for s, i in zip(scores[0].tolist(), idxs[0].tolist()):
            if i == -1:
                continue
            out.append((float(s), self.metas[i]))
        return out
