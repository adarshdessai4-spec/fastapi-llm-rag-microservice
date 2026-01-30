from pydantic import BaseModel, Field, HttpUrl

class IngestTextRequest(BaseModel):
    doc_id: str = Field(..., min_length=3, max_length=200)
    text: str = Field(..., min_length=10)

class IngestUrlRequest(BaseModel):
    doc_id: str = Field(..., min_length=3, max_length=200)
    url: HttpUrl

class ChatAnswerRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=2000)

class Citation(BaseModel):
    doc_id: str
    chunk_index: int
    snippet: str

class ChatAnswerResponse(BaseModel):
    answer: str
    citations: list[Citation]
