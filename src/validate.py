"""
validate.py

Validates transformed weather data before loading it into database
"""

import logging

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "location_name",
    "latitude",
    "longitude",
    "timezone",
    "observation_time",
    "date",
    "hour",
    "temperature_celsius",
    "humidity_percent",
    "precipitaion_nm",
    "wind_speed_kmh",
]

def validate_weather_data(df):
    """
    Validate transformed weather data.

    Args:
        df (pandas.Dataframe): Tranformed weather data.

    Returns:
        pandas.Dataframe: The same DataFrame if validation passes.

    Raises:
        ValueError: If validation fails.
    """

    try:
        logger.info("Starting weather data validation.")

        validate_required_columns(df)
        validate_missing_values(df)
        validate_duplicate_records(df)
        validate_weather_measurements(df)

        logger.info("Weather data validation completed successfully.")

        return df
    
    except ValueError as error:
        logger.error("Weather data validation failed: %s", error)
        raise