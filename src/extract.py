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

def validate_api_response(data):
    """
    Validate that the API response contains the required fields.

    Args:
        data (dict): Raw API response.

    Raises:
        ValueError: If requried fields are missing.
    """

    if "hourly" not in data:
        raise ValueError("Missing 'hourly' data in API response.")
    
    if "time" not in data["hourly"]:
        raise ValueError("Missing 'time' field in hourly data.")
    
    for variable in HOURLY_VARIABLES:
        if variable not in data["hourly"]:
            raise ValueError(f"Missing '{variable}' field in hourly data.")
        
    if len(data["hourly"]["time"]) == 0:
        raise ValueError("API response contains no hourly records.")