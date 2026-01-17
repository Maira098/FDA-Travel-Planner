import math
from clients.geocoding_client import GeocodingClient
from clients.weather_client import WeatherClient

class TravelDataAggregator:
    """
    Aggregates travel-related data from multiple APIs.
    """

    def __init__(self):
        self._geo_client = GeocodingClient()
        self._weather_client = WeatherClient()

    def _calculate_distance(self, lat1, lon1, lat2, lon2) -> float:
        """
        Calculate distance between two coordinates (Haversine formula).
        """
        R = 6371  # Earth radius in km

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2) ** 2 +
            math.cos(phi1) * math.cos(phi2) *
            math.sin(delta_lambda / 2) ** 2
        )

        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    def get_travel_summary(self, city_a: str, city_b: str) -> dict:
        """
        Get weather in city A and distance from city B.
        """
        coords_a = self._geo_client.fetch(city_a)
        coords_b = self._geo_client.fetch(city_b)

        weather = self._weather_client.fetch(
            coords_a["lat"], coords_a["lon"]
        )

        distance = self._calculate_distance(
            coords_a["lat"], coords_a["lon"],
            coords_b["lat"], coords_b["lon"]
        )

        return {
            "destination": city_a,
            "temperature": weather["temperature"],
            "weather": weather["description"],
            "distance_km": round(distance, 2)
        }
