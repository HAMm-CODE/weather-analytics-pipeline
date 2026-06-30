import requests
import logging

logger = logging.getLogger(__name__)

API_URL = "https://api.open-meteo.com/v1/forecast"

def extract():
    """
    To extract data from the open meteo API
    
    Returns:
        dict:Raw data extracted from the API in JSON format.
    """   
    #Tampere coordinates
    latitude = 61.4978
    longitude = 23.761

    # Parameters sent to the API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_sum",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Europe/Helsinki",
        "forecast_days": 7
    }

    try:
        logger.info("Starting weather data extraction from Open-Meteo API.")

        response = requests.get(API_URL, params=params, timeout=30)

        # Raise an error if the API request failed
        response.raise_for_status()

        data = response.json()

        # Basic response validation
        if "hourly" not in data:
            raise ValueError("Missing 'hourly' data in API response.")

        if "time" not in data["hourly"]:
            raise ValueError("Missing 'time' field in hourly data.")

        logger.info("Weather data extraction completed successfully.")

        return data

    except requests.exceptions.RequestException as error:
        logger.error("API request failed: %s", error)
        raise

    except ValueError as error:
        logger.error("Invalid API response: %s", error)
        raise
