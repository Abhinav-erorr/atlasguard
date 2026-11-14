"""Health endpoint tests."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_versioned_health_returns_ok() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_not_found_uses_structured_error() -> None:
    response = client.get("/missing")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "HTTP_ERROR"
    assert response.headers["X-Request-ID"] == response.json()["error"]["request_id"]