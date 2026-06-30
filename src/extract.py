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