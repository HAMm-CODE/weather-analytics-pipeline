"""
extract.py

Extract weather data from the Open-Mateo API
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
    REQUEST_TIMEOUT,
)

logger = logging.getLogger(__name__)

def extract_weather_data():
    """
    Extract weather data from the Open-Mateo API for one location

    Returns:
        dict: Raw weather data from the API.
    """

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": ",".join(HOURLY_VARIABLES),
        "timezone": TIMEZONE,
        "forecast_days": FORECAST_DAYS,
    }

    try:
        logger.info("Starting weather data extraction for %s.", LOCATION_NAME)

        response = requests.get(
            API_URL,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        validate_api_response(data)

        data["location_name"] = LOCATION_NAME

        logger.info("Weather data extraction completed successfully.")

        return data
    
    except requests.exceptions.RequestException as error:
        logger.error("API request failed: %s", error)
        raise

