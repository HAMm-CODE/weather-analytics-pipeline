"""
pipeline.py

Define the main ETL pipeline class for the Weather Analytics Project.
"""

import logging

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from src.load import load_weather_data


logger = logging.getLogger(__name__)


class WeatherETLPipeline:
    """
    A reusable class that runs the full weather ETL pipeline.

    Pipeline steps:
    1. Extract data from Open-Meteo API
    2. Trasform raw JSON into a clean DataFrame
    3. Validate the transformed data
    4. Load the data into the SQL database
    """

    def run(self):
        """
        Run the full ETL pipeline.
        """

        try:
            logger.info("Weather ETL pipeline started.")

            raw_weather_data = extract_weather_data()

            clean_weather_data = transform_weather_data(raw_weather_data)

            validated_weather_data = validate_weather_data(clean_weather_data)

            load_weather_data(validated_weather_data)

            logger.info("Weather ETL pipeline completed successfully.")

        except Exception as error:
            logger.error("Weather ETL pipeline failed: %s", error)
            raise