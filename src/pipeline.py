"""
pipeline.py

Define the main ETL pipeline class for the Weather Analytics Project.
"""

import logging

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from src.load import load_weather_data

