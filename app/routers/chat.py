from fastapi import APIRouter, Depends, Request

from app.deps import get_chat_service, get_rate_limiter
from app.schemas import ChatAnswerRequest, ChatAnswerResponse
from app.services.chat_service import ChatService
from app.services.rate_limit import SimpleRateLimiter

router = APIRouter()

@router.post("/answer", response_model=ChatAnswerResponse)
async def chat_answer(
    payload: ChatAnswerRequest,
    request: Request,
    limiter: SimpleRateLimiter = Depends(get_rate_limiter),
    svc: ChatService = Depends(get_chat_service),
):
    limiter.check(request)
    answer, citations = await svc.answer(payload.question)
    return ChatAnswerResponse(answer=answer, citations=citations)
