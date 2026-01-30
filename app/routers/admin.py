from fastapi import APIRouter, Depends
from app.deps import get_store
from app.services.vector_store import FaissVectorStore

router = APIRouter()

@router.get("/stats")
def stats(store: FaissVectorStore = Depends(get_store)):
    return {"vectors": int(store.index.ntotal), "chunks": len(store.metas)}
