from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# ========== Successful creation ==========
def test_create_user_success_integration():
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


# ========== Missing required fields (422 errors) ==========
def test_create_user_integration_422_missing_name():
    payload = {
        "email": "john@example.com"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 422


def test_create_user_integration_422_missing_email():
    payload = {
        "name": "John Doe"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 422
