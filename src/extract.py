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

