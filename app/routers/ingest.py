from fastapi import APIRouter, Depends, Request

from app.deps import get_ingest_service, get_rate_limiter
from app.schemas import IngestTextRequest, IngestUrlRequest
from app.services.ingest_service import IngestService
from app.services.rate_limit import SimpleRateLimiter

router = APIRouter()

@router.post("/text")
def ingest_text(
    payload: IngestTextRequest,
    request: Request,
    limiter: SimpleRateLimiter = Depends(get_rate_limiter),
    svc: IngestService = Depends(get_ingest_service),
):
    limiter.check(request)
    n = svc.ingest_text(payload.doc_id, payload.text)
    return {"ingested_chunks": n}

@router.post("/url")
async def ingest_url(
    payload: IngestUrlRequest,
    request: Request,
    limiter: SimpleRateLimiter = Depends(get_rate_limiter),
    svc: IngestService = Depends(get_ingest_service),
):
    limiter.check(request)
    n = await svc.ingest_url(payload.doc_id, str(payload.url))
    return {"ingested_chunks": n}
