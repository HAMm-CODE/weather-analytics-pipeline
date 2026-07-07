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

        # validate_required_columns(df)
        validate_missing_values(df)
        validate_duplicate_records(df)
        validate_weather_measurements(df)

        logger.info("Weather data validation completed successfully.")

        return df
    
    except ValueError as error:
        logger.error("Weather data validation failed: %s", error)
        raise

def validate_missing_values(df):
    """
    Check for missining in important columns.

    Args:
        df (pandas.DataFrame): Transformed weather data

    Raises:
        ValueError:If important columns contain missing values.
    """

    important_columns = [
        "location_name",
        "observation_time",
        "temperature_celsius",
        "humidity_percent",
    ]

    missing_values = df[important_columns].isnull().sum()

    columns_with_missing_values = missing_values[missing_values > 0]

    if not columns_with_missing_values.empty:
        raise ValueError(
            "Missing Values found in important columns: "
            f"{columns_with_missing_values.to_dict()}"
        )
    
def validate_duplicate_records(df):
    """
    Check for duplicate records based on location and observation time.

    Args:
        df (pandas.DataFrame): Transformed weather data.

    Raises:
        ValueError: If duplicate records are found.
    """

    duplicate_count =df.duplicated(
        subset=["location_name", "observation_time",]
    ).sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Found {duplicate_count} duplicate weather records."
        )


def validate_weather_measurements(df):
    """
    Validate weather measurement ranges.

    Args:
        df (pandas.DataFrame): Transformed weather data.

    Raises:
        ValueError: If weather values are outside realistic ranges.
    """
    
    if not df["temperature_celsius"].between(-80, 60).all():
        raise ValueError("Temperature values must be between -80°C and 50°C ")

    if not df["humidity_percent"].between(0, 100).all():
        raise ValueError("Humidity values must be between 0  and 100°C ")

    if not (df["precipitation_nm"] >= 0).all():
        raise ValueError("Precipitation cannot be negative")

    if not (df["wind_speed_kmh"] >= 0).all():
        raise ValueError("Wind Speed cannot be negative")

    if not df["hour"].between(0, 23).all():
        raise ValueError(
            "Hour values must be between 0 and 23."
        )