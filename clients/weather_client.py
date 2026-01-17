import os
import requests
import logging
from .base_client import AbstractAPIClient

class WeatherClient(AbstractAPIClient):
    """
    Client for fetching current weather data from OpenWeatherMap.
    """

    def __init__(self):
        self._api_key = os.getenv("OPENWEATHER_API_KEY")
        self._base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, lat: float, lon: float) -> dict:
        """
        Fetch current weather for given coordinates.
        """
        try:
            response = requests.get(
                self._base_url,
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": self._api_key,
                    "units": "metric"
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            return {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }

        except (KeyError, IndexError):
            logging.error("Unexpected weather data structure.")
            raise

        except requests.exceptions.RequestException as e:
            logging.error(f"Weather API error: {e}")
            raise
