# src/prompts/itinerary_prompt.py

ITINERARY_SYSTEM_MSG = """You are an expert trip planner.
- Write clear, day-wise itineraries with morning/afternoon/evening blocks.
- Balance travel time, budget, interests, and opening hours.
- Prefer nearby attractions on the same day to reduce transit.
- Add 1–2 food/stay suggestions/day when helpful.
- Output concise, structured Markdown.
"""

ITINERARY_TEMPLATE = """Plan a {days}-day trip to **{destination}** for {travelers} traveler(s).

Preferences:
- Interests: {interests}
- Budget level: {budget}
- Travel dates: {start_date} to {end_date}
- Origin city (for context): {origin}

Reference data (may be partial):
- Flights (sample or live): {flights}
- Hotels (sample or live): {hotels}
- Attractions (sample or live): {attractions}

Constraints:
- Keep walking/transit realistic.
- Avoid closed attractions if dates are provided.
- End each day with a short summary.

Return only the itinerary in Markdown.
"""
