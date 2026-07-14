"""
elt.py

Implements a simple ELT workflow for the Weather Analytics project.

ELT flow:
1. Extract raw weather data from Open-Meteo API
2. Load raw JSON into the staging table
3. Read raw data from staging
4. Transform the staged raw data
5. Validate the transformed data
6. Load the clean data into the final star schema
"""

import json
import logging
import sqlite3

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from src.load import (
    create_tables,
    get_database_connection,
    load_weather_data,
)

logger = logging.getLogger(__name__)


def load_raw_weather_data_to_staging(raw_data):
    """
    Load raw weather API JSON into the staging table.

    Args:
        raw_data (dict): Raw weather data extracted from the API.
    """

    connection = None

    try:
        logger.info("Starting raw weather data load into staging table.")

        connection = get_database_connection()
        create_tables(connection)

        insert_query = """
            INSERT INTO stg_weather_raw (
                location_name,
                latitude,
                longitude,
                timezone,
                raw_json
            )
            VALUES (?, ?, ?, ?, ?);
        """

        connection.execute(
            insert_query,
            (
                raw_data.get("location_name"),
                raw_data.get("latitude"),
                raw_data.get("longitude"),
                raw_data.get("timezone"),
                json.dumps(raw_data),
            ),
        )

        connection.commit()

        logger.info("Raw weather data loaded into staging table successfully.")

    except sqlite3.Error as error:
        logger.error("Failed to load raw weather data into staging: %s", error)
        raise
    
    finally:
        if connection:
            connection.close()
            logger.info("Database connection closed after staging load.")


def get_latest_raw_weather_data_from_staging():
    """
    Retrieve the latest raw weather JSON record from the staging table.

    Returns:
        dict: Raw weather data loaded from the staging table.
    """

    connection = None

    try:
        logger.info("Reading latest raw weather data from staging table.")

        connection = get_database_connection()
        create_tables(connection)

        query = """
            SELECT raw_json
            FROM stg_weather_raw
            ORDER BY raw_id DESC
            LIMIT 1;
        """

        result = connection.execute(query).fetchone()

        if result is None:
            raise ValueError("No raw weather data found in staging table.")

        raw_json = result[0]
        raw_data = json.loads(raw_json)

        logger.info("Latest raw weather data retrieved from staging table.")

        return raw_data

    except sqlite3.Error as error:
        logger.error("Failed to read raw weather data from staging: %s", error)
        raise

    finally:
        if connection:
            connection.close()
            logger.info("Database connection closed after staging read.")


class WeatherELTWorkflow:
    """
    A reusable class that runs the simple ELT workflow.

    ELT steps:
    1. Extract raw data from the API
    2. Load raw data into staging table
    3. Read staged raw data
    4. Transform staged data
    5. Validate transformed data
    6. Load clean data into final star schema
    """

    def run(self):
        """
        Run the full ELT workflow.
        """

        try:
            logger.info("Weather ELT workflow started.")

            raw_weather_data = extract_weather_data()

            load_raw_weather_data_to_staging(raw_weather_data)

            staged_raw_weather_data = get_latest_raw_weather_data_from_staging()

            clean_weather_data = transform_weather_data(staged_raw_weather_data)

            validated_weather_data = validate_weather_data(clean_weather_data)

            load_weather_data(validated_weather_data)

            logger.info("Weather ELT workflow completed successfully.")
            
        except Exception as error:
            logger.error("Weather ELT workflow failed: %s", error)
            raise