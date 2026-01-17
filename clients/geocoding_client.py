import os
import requests
import logging
from .base_client import AbstractAPIClient

class GeocodingClient(AbstractAPIClient):
    """
    Client for converting city names to coordinates using OpenCage API.
    """

    def __init__(self):
        self._api_key = os.getenv("OPENCAGE_API_KEY")
        self._base_url = "https://api.opencagedata.com/geocode/v1/json"

    def fetch(self, city: str) -> dict:
        """
        Fetch latitude and longitude for a city.
        """
        try:
            response = requests.get(
                self._base_url,
                params={"q": city, "key": self._api_key},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            if not data["results"]:
                raise ValueError("No geocoding results found.")

            location = data["results"][0]["geometry"]
            return {
                "lat": location["lat"],
                "lon": location["lng"]
            }

        except requests.exceptions.RequestException as e:
            logging.error(f"Geocoding API error: {e}")
            raise
