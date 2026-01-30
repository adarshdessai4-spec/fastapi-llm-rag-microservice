import time
from dataclasses import dataclass
from typing import Dict, Tuple

from fastapi import HTTPException, Request
from app.config import settings

@dataclass
class SimpleRateLimiter:
    buckets: Dict[str, Tuple[int, float]]

    def __init__(self):
        self.buckets = {}

    def key(self, request: Request) -> str:
        return request.client.host if request.client else "unknown"

    def check(self, request: Request) -> None:
        k = self.key(request)
        now = time.time()
        count, start = self.buckets.get(k, (0, now))
        if now - start >= 60:
            count, start = 0, now
        count += 1
        self.buckets[k] = (count, start)
        if count > settings.rate_limit_rpm:
            raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")
