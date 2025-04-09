import pytest
from lib import allocate_vehicles_to_listings

def test_successful_allocation():
    vehicle_requests = [
        {"length": 10, "quantity": 2},
        {"length": 20, "quantity": 1}
    ]
    listings = [
        {"id": "a", "length": 10, "width": 20, "location_id": "loc1", "price_in_cents": 100},
        {"id": "b", "length": 10, "width": 20, "location_id": "loc1", "price_in_cents": 150},
        {"id": "c", "length": 20, "width": 20, "location_id": "loc1", "price_in_cents": 200}
    ]
    result = allocate_vehicles_to_listings(vehicle_requests, listings)
    assert result is not None
    assert set(result["listing_ids"]) == {"a", "b", "c"}
    assert result["total_price_in_cents"] == 450

def test_allocation_fails_insufficient_listings():
    vehicle_requests = [
        {"length": 10, "quantity": 3}
    ]
    listings = [
        {"id": "a", "length": 10, "width": 20, "location_id": "loc1", "price_in_cents": 100},
        {"id": "b", "length": 10, "width": 20, "location_id": "loc1", "price_in_cents": 150}
    ]
    result = allocate_vehicles_to_listings(vehicle_requests, listings)
    assert result is None