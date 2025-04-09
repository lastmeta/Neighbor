import json
import pytest
from main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_non_list_payload(client):
    res = client.post("/", json={"length": 10})
    assert res.status_code == 400
    assert "expected a list" in res.get_json()["error"]

def test_missing_keys(client):
    res = client.post("/", json=[{"length": 10}])
    assert res.status_code == 400
    assert "must have 'length' and 'quantity'" in res.get_json()["error"]

def test_non_integer_values(client):
    res = client.post("/", json=[{"length": "ten", "quantity": 2}])
    assert res.status_code == 400
    assert "'length' and 'quantity' must be integers" in res.get_json()["error"]

def test_valid_input_returns_200(client):
    res = client.post("/", json=[{"length": 10, "quantity": 1}])
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)