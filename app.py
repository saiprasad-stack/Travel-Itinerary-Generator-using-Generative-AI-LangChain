# app.py
import streamlit as st
from datetime import date, timedelta

from src.prompts.itinerary_prompt import ITINERARY_SYSTEM_MSG, ITINERARY_TEMPLATE
from src.services.llm import generate_itinerary
from src.services.providers import get_attractions, get_hotels, get_flights

st.set_page_config(page_title="AI Travel Itinerary Generator", page_icon="✈️")

st.title("✈️ Travel Itinerary Generator (LangChain + LLM)")
st.caption("By Prasad — personalized, day-wise plans powered by Generative AI")

with st.form("trip_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input("Destination city", value="Paris")
        origin = st.text_input("Origin city", value="Hyderabad")
        days = st.number_input("Trip length (days)", min_value=1, max_value=30, value=4)
    with col2:
        start_date = st.date_input("Start date", value=date.today() + timedelta(days=14))
        budget = st.selectbox("Budget", ["budget", "mid", "premium"], index=1)
        travelers = st.number_input("Travelers", min_value=1, max_value=10, value=1)

    interests = st.multiselect(
        "Interests",
        ["culture", "history", "food", "nightlife", "shopping", "beaches", "adventure", "nature"],
        default=["culture", "food"],
    )

    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    st.info("Generating itinerary…")

    # Collect “live or sample” data
    flights = get_flights(origin, destination, start_date.isoformat())
    hotels = get_hotels(destination, budget)
    attractions = get_attractions(destination, interests)

    params = {
        "days": int(days),
        "destination": destination,
        "travelers": int(travelers),
        "interests": ", ".join(interests) if interests else "general sightseeing",
        "budget": budget,
        "start_date": start_date.isoformat(),
        "end_date": (start_date + timedelta(days=int(days)-1)).isoformat(),
        "origin": origin,
        "flights": flights,
        "hotels": hotels,
        "attractions": attractions
    }

    try:
        itinerary_md = generate_itinerary(params, ITINERARY_SYSTEM_MSG, ITINERARY_TEMPLATE)
        st.success("Done!")
        st.markdown(itinerary_md)
        st.download_button("⬇️ Download Itinerary (Markdown)", itinerary_md, file_name="itinerary.md")
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

st.caption("Tip: Replace sample providers with real APIs (Amadeus/Skyscanner/Google Places) when ready.")
