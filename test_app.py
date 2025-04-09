import json
import pytest
from main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_search_vehicles_success(client):
    payload = [
        {"length": 10, "quantity": 1},
        {"length": 20, "quantity": 2},
        {"length": 25, "quantity": 1}
    ]
    response = client.post("/", data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 200
    results = response.get_json()
    assert isinstance(results, list)
    for result in results:
        assert "location_id" in result
        assert "listing_ids" in result
        assert "total_price_in_cents" in result