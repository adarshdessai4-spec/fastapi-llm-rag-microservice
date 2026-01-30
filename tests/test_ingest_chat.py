from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_and_chat():
    r = client.post("/v1/ingest/text", json={"doc_id": "doc1", "text": "FastAPI is a modern web framework for building APIs."})
    assert r.status_code == 200

    r2 = client.post("/v1/chat/answer", json={"question": "What is FastAPI?"})
    assert r2.status_code == 200
    data = r2.json()
    assert "answer" in data
    assert "citations" in data
    assert len(data["citations"]) >= 1
