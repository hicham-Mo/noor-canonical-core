from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_law_compliance():
    response = client.get("/compliance/law-42-25")
    assert response.status_code == 200
    assert response.json()["law"] == "Loi 42.25"
