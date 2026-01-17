import logging
from dotenv import load_dotenv
from aggregator import TravelDataAggregator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

if __name__ == "__main__":
    planner = TravelDataAggregator()

    city_a = input("Enter destination city: ")
    city_b = input("Enter reference city: ")

    result = planner.get_travel_summary(city_a, city_b)

    print("\nTravel Summary")
    print("----------------")
    print(f"Destination: {result['destination']}")
    print(f"Weather: {result['weather']}")
    print(f"Temperature: {result['temperature']}°C")
    print(f"Distance from {city_b}: {result['distance_km']} km")
