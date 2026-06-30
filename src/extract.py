"""
extract.py

Etracts weather data from the Open-Meteo API.
"""

import logging
import requests

from src.config import (
    API_URL,
    LATITUDE,
    LONGITUDE,
    LOCATION_NAME,
    HOURLY_VARIABLES,
    FORECAST_DAYS,
    TIMEZONE,
    REQUEST_TIMEOUT
)

logger = logging.getLogger(__name__)

def extract_weather_data():
    """
    Exract weather data from the Open-Meteo API.

    Returns:
        dict: A dictionary containing the extracted weather data.
    """
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": ",".join(HOURLY_VARIABLES),
        "forecast_days": FORECAST_DAYS,
        "timezone": TIMEZONE
    }