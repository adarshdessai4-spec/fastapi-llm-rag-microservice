from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Sequence

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config import settings

@dataclass
class ContextChunk:
    doc_id: str
    chunk_index: int
    text: str

class LLM(Protocol):
    async def answer(self, question: str, context: Sequence[ContextChunk]) -> str: ...

class StubLLM:
    async def answer(self, question: str, context: Sequence[ContextChunk]) -> str:
        if not context:
            return "I don't have enough context to answer confidently."
        best = context[0].text
        return f"Based on the provided context, here's a grounded response: {best[:320]}"

class OpenAILLM:
    def __init__(self, api_key: str):
        self.api_key = api_key

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(min=1, max=4))
    async def answer(self, question: str, context: Sequence[ContextChunk]) -> str:
        ctx = "\n\n".join([f"[{c.doc_id}#{c.chunk_index}] {c.text}" for c in context])
        system = (
            "You are a helpful assistant. Answer ONLY using the provided CONTEXT. "
            "If the answer is not in the context, say you don't know."
        )
        user = f"QUESTION: {question}\n\nCONTEXT:\n{ctx}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        timeout = httpx.Timeout(settings.request_timeout_seconds)
        async with httpx.AsyncClient(timeout=timeout) as client:
            r = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    "temperature": 0.2,
                },
            )
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"].strip()

def get_llm() -> LLM:
    if settings.llm_provider == "openai":
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is required for LLM_PROVIDER=openai")
        return OpenAILLM(settings.openai_api_key)
    return StubLLM()
