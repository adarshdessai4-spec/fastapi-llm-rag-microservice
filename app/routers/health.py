from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/")
def home():
    return {
        "service": "FastAPI LLM-RAG Microservice",
        "docs": "/docs",
        "health": "/health"
    }
