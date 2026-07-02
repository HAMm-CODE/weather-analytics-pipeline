"""
main.py

Entry point running the weather ETL project manually
"""

import logging

from src.extract import extract_weather_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log")
        logging.StreamHandler(),
    ],
)

