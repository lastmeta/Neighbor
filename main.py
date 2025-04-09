from flask import Flask, request, jsonify
import json
from lib import find_valid_locations

app = Flask(__name__)
listings = []

# For tests
def create_app():
    global listings
    with open('listings.json') as f:
        listings = json.load(f)
    return app

# Load listings once at startup
with open('listings.json') as f:
    listings = json.load(f)


@app.route('/', methods=['POST', 'GET'])
def search_vehicles():
    if request.method == 'POST':
        vehicle_requests = request.get_json()

        if not isinstance(vehicle_requests, list):
            return jsonify({"error": "Invalid input: expected a list of vehicle requests"}), 400

        for item in vehicle_requests:
            if not isinstance(item, dict) or "length" not in item or "quantity" not in item:
                return jsonify({"error": "Invalid vehicle request: each item must have 'length' and 'quantity'"}), 400
            if not isinstance(item["length"], int) or not isinstance(item["quantity"], int):
                return jsonify({"error": "'length' and 'quantity' must be integers"}), 400

        results = find_valid_locations(listings, vehicle_requests)
        return jsonify(results)

    if request.method == 'GET':
        return jsonify({"message": "Welcome to the Vehicle API, please make a POST request."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
