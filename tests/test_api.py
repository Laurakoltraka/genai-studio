from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_chat_rejects_empty_message():
    response = client.post(
        "/api/v1/chat",
        json={
            "message": "",
            "provider": "huggingface",
        },
    )

    assert response.status_code == 422