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
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler(),
    ],
)

if __name__ == "__main__":
    weather_data = extract_weather_data()

    print("Extraction successful!")
    print("Location:", weather_data["location_name"])
    print("Hourly fields:", weather_data["hourly"].keys())
    print("First 5:", weather_data["hourly"]["time"][:5])

