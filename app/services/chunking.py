from typing import List

def chunk_text(text: str, max_chars: int = 800, overlap: int = 120) -> List[str]:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_chars)
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks
