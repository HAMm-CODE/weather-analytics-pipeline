"""
transform.py

Transforms raw Open-Mateo API data into a clean tabular format
"""

import logging

import pandas as pd

logger = logging.getLogger(__name__)

def transform_weather_data(raw_data):
    """
    Transform raw weather API data into a clean Pandas DataFrame

    Args:
        raw_data (dict): Raw JSON data from the Open-Mateo API.

    Returns:
        pandas.DataFrame: Cleaned weather data.
    """

    try:
        logger.info("Starting weather data transformation.")

        if "hourly" not in raw_data:
            raise ValueError("Raw data does not contain 'hourly' field.")
        
        hourly_data = raw_data["hourly"]

        #convert hourly JSON data into a DataFrame
        df = pd.DataFrame(hourly_data)

        """So here we create a dataframe df and parse in hourly data and then add dataframe columns or attributes 
        from the raw_data variable that contains raw data from the api"""
        # Add Location metadata
        df["location_name"] = raw_data.get("location_name", "unknown")
        df["latitude"] = raw_data.get("latitude")
        df["longitude"] = raw_data.get("longitude")
        df["timezone"] = raw_data.get("timezone")

        # Rename columns to cleaner names
        df = df.rename(
            columns={
                "time": "observation_time",
                "temperature_2m": "temperature_celsius",
                "relative_humidity_2m": "humidity_percent",
                "precipitation": "precipitation_nm",
                "wind_speed_10m": "wind_speed_kmh"
            }
        )

        #convert timestamp column to datetime
        df["observation_time"] = pd.to_datetime(
            df["observation_time"],
            errors="coerce"
        )

        #convert numeric columns to proper numeric types
        numeric_columns = [
            "temperature_celcius",
            "humidity_percent",
            "precipitation_nm",
            "wind_speed_kmh",
            "latitude",
            "longitude",
        ] 

        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")
        
        # Standardize Location name
        df["location_name"] = df["location_name"].str.strip().str.title()

        # Create derived fields for easier analysis and star schema loading
        df["date"] = df["observation_time"].dt.date
        df["hour"] = df["observation_time"].dt.hour

        #Remove duplicate weather records
        df = df.drop_duplicates(
            subset = ["location_name", "observation_time"]
        )

        #Handle missing values in important fields
        df = df.dropna(
            subset=[
                "observation_time",
                "temperature_celsius",
                "humidity_percent"
            ]
        )

        # Reoder columns for readability
        df = df[
            [
                "location_name",
                "latitude",
                "longitude",
                "timezone",
                "observation_time",
                "date",
                "hour",
                "temperature_celsius",
                "humidity_percent",
                "preciptation_nm",
                "wind_speed_kmh",
            ]
        ]

        logger.info(
            "Weather data transformation completed successfully. Rows: %s",
            len(df),
        )

        return df

    except Exception as error:
        logger.error("Weather data tranformation failed: %s", error)
        raise