# src/services/providers.py
from typing import List, Dict

# ------- Fallback sample data (works offline) -------
SAMPLE_ATTRACTIONS = {
    "paris": [
        {"name": "Louvre Museum", "area": "1st arrondissement", "rating": 4.8},
        {"name": "Eiffel Tower", "area": "Champ de Mars", "rating": 4.7},
        {"name": "Montmartre & Sacré-Cœur", "area": "18th arrondissement", "rating": 4.7},
        {"name": "Seine River Cruise", "area": "Seine", "rating": 4.6},
    ],
    "goa": [
        {"name": "Baga Beach", "area": "North Goa", "rating": 4.5},
        {"name": "Basilica of Bom Jesus", "area": "Old Goa", "rating": 4.6},
        {"name": "Aguada Fort", "area": "Candolim", "rating": 4.4},
        {"name": "Palolem Beach", "area": "South Goa", "rating": 4.7},
    ],
}

SAMPLE_HOTELS = {
    "paris": [
        {"name": "Hôtel Des Arts Montmartre", "area": "Montmartre", "price_level": "mid"},
        {"name": "CitizenM Paris Champs-Élysées", "area": "8th", "price_level": "mid"},
        {"name": "Ibis Paris Tour Eiffel", "area": "15th", "price_level": "budget"},
    ],
    "goa": [
        {"name": "Taj Fort Aguada", "area": "Candolim", "price_level": "premium"},
        {"name": "Lemon Tree Candolim", "area": "Candolim", "price_level": "mid"},
        {"name": "Zostel Goa", "area": "Anjuna", "price_level": "budget"},
    ],
}

SAMPLE_FLIGHTS = lambda origin, dest, start_date: [
    {"route": f"{origin.upper()} → {dest.upper()}", "date": start_date, "notes": "Sample flight data for demo"}
]

# ------- Public API adapters (stubs to replace later) -------
def get_attractions(city: str, interests: List[str]) -> List[Dict]:
    city_key = city.strip().lower()
    return SAMPLE_ATTRACTIONS.get(city_key, [])

def get_hotels(city: str, budget: str) -> List[Dict]:
    city_key = city.strip().lower()
    hotels = SAMPLE_HOTELS.get(city_key, [])
    if budget:
        b = budget.lower()
        # naive filter
        if b in ["budget", "mid", "premium"]:
            hotels = [h for h in hotels if h["price_level"] == b] or hotels
    return hotels

def get_flights(origin: str, destination: str, start_date: str):
    # Return sample for MVP; swap with real Amadeus/Skyscanner later
    return SAMPLE_FLIGHTS(origin, destination, start_date)
