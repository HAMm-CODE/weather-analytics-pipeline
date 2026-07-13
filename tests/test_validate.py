"""
test_validate.py

Unit tests for src/validate.py
"""

import pandas as pd
import pytest

from src.validate import validate_weather_data

def create_valid_weather_dataframe():
    return pd.DataFrame(
        {
            "location_name": ["Tampere"],
            "latitude": [61.4991],
            "longitude": [23.7871],
            "timezone": ["Europe/Helsinki"],
            "observation_time": [pd.Timestamp("2026-07-09 00:00:00")],
            "date": [pd.to_datetime("2026-07-09").date()],
            "hour": [0],
            "temperature_celsius": [15.5],
            "humidity_percent": [80],
            "precipitation_mm": [0.0],
            "wind_speed_kmh": [8.5],
        }
    )
