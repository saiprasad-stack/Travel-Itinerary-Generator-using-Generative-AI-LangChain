# Travel-Itinerary-Generator-using-Generative-AI-LangChain
An AI-powered travel planner that generates personalized, day-wise itineraries based on user preferences (destination, budget, duration, interests). Built with Python, Streamlit, LangChain, and Hugging Face LLMs.
🧳 Travel Itinerary Generator using Generative AI & LangChain
📌 Overview

The Travel Itinerary Generator is an AI-powered web app that creates personalized, day-wise travel plans based on user preferences such as destination, budget, trip duration, and interests.

It leverages Generative AI models (via Hugging Face + LangChain) to generate structured itineraries, while allowing integration with real-world travel APIs for flights, hotels, and attractions.

🚀 Built with Python + Streamlit + LangChain + Hugging Face, this project demonstrates how AI + APIs + interactive UI can solve real-world travel planning problems.

✨ Features

✅ Generate custom travel itineraries (day-wise: morning, afternoon, evening).

✅ Input destination, trip duration, budget, interests, travelers, dates.

✅ Uses Generative AI models (Zephyr-7B, Mistral, Flan-T5, etc.).

✅ Sample flights, hotels, attractions data included.

✅ Streamlit web app UI (interactive form + Markdown output).

✅ Download itinerary as a Markdown file.

✅ Future-ready for real API integration (Amadeus, Google Places).

🏗️ Project Structure
travel-itinerary-ai/
  ├─ .env                  # API keys (Hugging Face, Amadeus, Google Places)
  ├─ requirements.txt      # Python dependencies
  ├─ app.py                # Streamlit main app
  └─ src/
     ├─ prompts/
     │  └─ itinerary_prompt.py   # Prompt templates for itinerary generation
     ├─ services/
     │  ├─ llm.py               # LLM integration (Hugging Face + LangChain)
     │  └─ providers.py         # Data providers (sample flights/hotels/attractions)
     └─ utils/
        └─ __init__.py          # Placeholder for utility functions

🛠️ Tech Stack

Python – Core programming language

Streamlit – Interactive web app UI

LangChain – LLM orchestration & prompt management

Hugging Face (Inference API) – Free/open-source LLMs

dotenv – Secure API key management

Requests / Pandas – API calls & data handling

📌 Why These Tools?

Python → Industry standard for AI/ML projects.

LangChain → Simplifies working with LLMs, prompt templates, and chains.

Hugging Face → Free alternative to OpenAI for Generative AI models.

Streamlit → Quick, elegant frontend without needing React/HTML.

dotenv → Keeps API keys secure and out of code.

Requests/Pandas → API integration & structured data management.

⚙️ Setup & Installation

Clone the repo

git clone https://github.com/your-username/travel-itinerary-ai.git
cd travel-itinerary-ai


Create virtual environment

python -m venv .venv
.venv\Scripts\activate   # (Windows)
source .venv/bin/activate # (Mac/Linux)


Install dependencies

pip install -r requirements.txt


Setup .env file
Create a .env file in the project root:

HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxx
# Optional (for real APIs):
AMADEUS_API_KEY=
AMADEUS_API_SECRET=
GOOGLE_PLACES_API_KEY=


Run the app

streamlit run app.py


Open http://localhost:8501
 in your browser 🎉

📷 Screenshots (add after running)

🖼️ Streamlit input form

🖼️ Generated itinerary output

🚀 Future Improvements

🔗 Integrate real APIs (Amadeus, Google Places) for live data.

🗺️ Add maps & images for attractions.

💾 Export itinerary to PDF/JSON.

🌐 Deploy on Streamlit Cloud / Hugging Face Spaces for public access.

👨‍💻 Author

Prasad – CSE (AI & ML) Graduate | Aspiring AI Generalist
💡 Passionate about AI/ML, NLP, Generative AI, and real-world applications.
