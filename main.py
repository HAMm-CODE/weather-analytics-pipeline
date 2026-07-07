"""
main.py

Entry point running the weather ETL project manually
"""

import logging

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler(),
    ],
)

if __name__ == "__main__":
    raw_weather_data = extract_weather_data()

    clean_weather_data = transform_weather_data(raw_weather_data)

    validated_weather_data = validate_weather_data(clean_weather_data)

    print("Extraction, transformation, and validation successful!")
    print(validated_weather_data.head())
    print(validated_weather_data.info())

