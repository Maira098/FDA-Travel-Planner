Personalized Travel Planner
Federated Data Aggregator (FDA)
NAMES: SANA TARIQ (058), MAIRA MALIK (040)
SUBMITTED TO: SIR SHEHZAD
1. Problem Statement

Modern applications often rely on multiple external services (APIs) to function effectively.
This project solves the problem of fragmented external data by implementing a Federated Data Aggregator (FDA).

The Personalized Travel Planner aggregates data from multiple public APIs to provide users with a unified travel summary. Instead of manually querying separate services, the application combines:

Geocoding data (city → latitude & longitude)

Weather data (current conditions)

into a single, coherent result.

2 . What the Application Does

Given:

A destination city

A reference city

The application:

Converts both city names into geographic coordinates.

Fetches current weather data for the destination city.

Calculates the distance between the two cities.

Presents the aggregated travel information in a single output.

This demonstrates federated data retrieval, transformation, and integration.

3 . APIs Used

OpenCage Geocoding API – Converts city names into latitude and longitude.

OpenWeatherMap API – Provides current weather data based on coordinates.

4 . Installation Instructions
Step 1: Clone or extract the project
cd fda-travel-planner
Step 2: (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
Step 3: Install dependencies
pip install -r requirements.txt
5 . API Key Setup (Secure Configuration)
Step 1: Create a .env file

Copy the provided example file:

cp .env.example .env

(Windows)

copy .env.example .env
Step 2: Add your API keys to .env
OPENWEATHER_API_KEY=your_openweathermap_api_key
OPENCAGE_API_KEY=your_opencage_api_key


6 . How to Run the Application

From the project root directory:

python main.py

You will be prompted to enter:

Destination city

Reference city

The application will then display:

Weather information for the destination

Distance between the two cities

7 . Project Structure
fda-travel-planner/
│
├── clients/
│   ├── base_client.py        # Abstract API client
│   ├── geocoding_client.py   # OpenCage client
│   └── weather_client.py     # OpenWeatherMap client
│
├── aggregator.py             # Data aggregation logic
├── main.py                   # Application entry point
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
8 . Notes

The application follows object-oriented design principles.

API-specific logic is encapsulated within individual client classes.

Errors such as network failures or invalid API responses are handled gracefully.

Logging is implemented to track successful operations and errors.

9 . Disclaimer

This project was developed for educational purposes as part of an open-ended laboratory assignment.
All APIs are used in accordance with their free-tier usage policies.