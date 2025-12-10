from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_controller_creates_user_successfully():
    payload = {
        "name": "John Doe",
        "email": "john@example.com"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["success"] is True
    assert data["message"] == "User created"
    assert data["user_id"] == 1


def test_controller_returns_422_when_name_missing():
    payload = {
        "email": "john@example.com"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 422


def test_controller_returns_422_when_email_missing():
    payload = {
        "name": "John Doe"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 422
