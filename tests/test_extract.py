"""
test_transform.py

Unit tests for src/transform.py
"""

from src.transform import transform_weather_data

def test_transform_weather_data_returns_clean_dataframe():
    raw_data = {
            "location_name": "Tampere",
            "latitude": 61.4991,
            "longitude": 23.7871,
            "timezone": "Europe/Helsinki",
            "hourly": {
                "time": ["2026-07-09T00:00", "2026-07-09T01:00"],
                "temperature_2m": [15.5, 16.2],
                "relative_humidity_2m": [80, 78],
                "precipitation": [0.0, 0.1],
                "wind_speed_10m": [8.5, 9.2],
        },
    }

    df = transform_weather_data(raw_data)

    