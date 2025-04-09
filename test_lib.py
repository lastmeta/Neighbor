import unittest
from lib import fits_vehicles, find_valid_locations

class TestBinPacking(unittest.TestCase):

    def test_fits_vehicles_exact_fit(self):
        listings = [
            {"id": "a", "length": 40, "width": 10, "location_id": "loc1", "price_in_cents": 100},
            {"id": "b", "length": 15, "width": 10, "location_id": "loc1", "price_in_cents": 150}
        ]
        vehicles = [
            {"length": 20, "quantity": 1},
            {"length": 15, "quantity": 1},
            {"length": 20, "quantity": 1},
        ]
        self.assertTrue(fits_vehicles(listings, vehicles))

    def test_fits_vehicles_too_short(self):
        listings = [
            {"id": "a", "length": 10, "width": 10, "location_id": "loc1", "price_in_cents": 100},
        ]
        vehicles = [
            {"length": 20, "quantity": 1},
        ]
        self.assertFalse(fits_vehicles(listings, vehicles))

    def test_fits_vehicles_insufficient_width(self):
        listings = [
            {"id": "a", "length": 50, "width": 5, "location_id": "loc1", "price_in_cents": 100},
        ]
        vehicles = [
            {"length": 10, "quantity": 1},
        ]
        self.assertFalse(fits_vehicles(listings, vehicles))

    def test_find_valid_locations(self):
        listings = [
            {"id": "l1", "length": 20, "width": 10, "location_id": "loc1", "price_in_cents": 100},
            {"id": "l2", "length": 20, "width": 10, "location_id": "loc1", "price_in_cents": 100},
            {"id": "l3", "length": 30, "width": 10, "location_id": "loc1", "price_in_cents": 150},
            {"id": "l4", "length": 50, "width": 10, "location_id": "loc2", "price_in_cents": 200},
        ]
        vehicles = [
            {"length": 20, "quantity": 2},
            {"length": 10, "quantity": 1},
        ]
        results = find_valid_locations(listings, vehicles)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["location_id"], "loc2")
        self.assertEqual(results[1]["location_id"], "loc1")
        self.assertLessEqual(results[0]["total_price_in_cents"], results[1]["total_price_in_cents"])

    def test_no_valid_locations(self):
        listings = [
            {"id": "l1", "length": 10, "width": 10, "location_id": "loc1", "price_in_cents": 100},
        ]
        vehicles = [
            {"length": 50, "quantity": 1},
        ]
        results = find_valid_locations(listings, vehicles)
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
