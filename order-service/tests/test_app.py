import sys
sys.path.append(".")

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Order Service is running"}


def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200

    data = response.json()
    assert "orders" in data
    assert len(data["orders"]) == 2
