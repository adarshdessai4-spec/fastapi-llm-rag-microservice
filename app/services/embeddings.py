import hashlib
from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class Embedder:
    dim: int = 384

    def embed(self, texts: List[str]) -> np.ndarray:
        # Lightweight deterministic embedding for demo (no external model download).
        vecs = []
        for t in texts:
            h = hashlib.sha256(t.encode("utf-8")).digest()
            raw = (list(h) * ((self.dim // len(h)) + 1))[: self.dim]
            arr = np.array(raw, dtype=np.float32)
            arr = (arr - arr.mean()) / (arr.std() + 1e-6)
            vecs.append(arr)
        return np.vstack(vecs)
