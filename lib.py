from itertools import combinations
from collections import defaultdict
import json

def fits_vehicles(listing_combo, vehicles):
    bins = []
    for l in listing_combo:
        if l["width"] >= 10:
            bins.append(l["length"])

    vehicles_flat = []
    for v in vehicles:
        vehicles_flat.extend([v["length"]] * v["quantity"])

    vehicles_flat.sort(reverse=True)

    for v in vehicles_flat:
        # Try to fit this vehicle in the tightest bin that fits it
        best_fit = -1
        min_leftover = float("inf")
        for i, space in enumerate(bins):
            if space >= v and (space - v) < min_leftover:
                best_fit = i
                min_leftover = space - v
        if best_fit == -1:
            return False
        bins[best_fit] -= v

    return True

def find_valid_locations(listings, vehicle_request):
    grouped = defaultdict(list)
    for l in listings:
        grouped[l["location_id"]].append(l)

    result = []
    for loc_id, loc_listings in grouped.items():
        best = None
        for r in range(1, min(6, len(loc_listings)+1)):
            for combo in combinations(loc_listings, r):
                if not all(l["width"] >= 10 for l in combo):
                    continue
                if fits_vehicles(combo, vehicle_request):
                    total_price = sum(l["price_in_cents"] for l in combo)
                    if best is None or total_price < best["total_price_in_cents"]:
                        best = {
                            "location_id": loc_id,
                            "listing_ids": [l["id"] for l in combo],
                            "total_price_in_cents": total_price
                        }
        if best:
            result.append(best)

    return sorted(result, key=lambda x: x["total_price_in_cents"])