import sys
sys.path.append(".")

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "User Service is running"}


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200

    data = response.json()
    assert "users" in data
    assert len(data["users"]) == 2


