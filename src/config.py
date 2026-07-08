"""
config.py

Stores configuration values for the weather ETL project.
"""

API_URL = "https://api.open-meteo.com/v1/forecast"

LOCATION_NAME = "Tampere"
LATITUDE = 61.4991
LONGITUDE = 23.7871

HOURLY_VARIABLES = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
]

FORECAST_DAYS = 1
TIMEZONE = "auto"
REQUEST_TIMEOUT = 30

DATABASE_PATH = "data/weather.db"
SQL_SCHEMA_PATH = "sql/create_table.sql"