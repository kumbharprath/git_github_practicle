from fastapi.testclient import TestClient
from app.main import app, add_numbers

client = TestClient(app)


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_greeting():
    response = client.get("/greet/Asha")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Asha!"


def test_add_api():
    response = client.post("/add", json={"a": 4, "b": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 9


def test_invalid_input():
    response = client.post("/add", json={"a": "wrong", "b": 5})
    assert response.status_code == 422
