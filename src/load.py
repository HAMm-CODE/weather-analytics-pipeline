"""
load.py

Loads validated weather data into a SQLite database using a star schema.
"""

import logging
import sqlite3

import pandas as pd

from src.config import DATABASE_PATH, SQL_SCHEMA_PATH

logger = logging.getLogger(__name__)

def get_database_connection():
    """
    Create and return a SQLite database connection.

    Returns:
        sqlite3.Connection: SQLite database connection.
    """

    try:
        connection = sqlite3.connect(DATABASE_PATH)
        connection.execute("PRAGMA foreign_keys = ON;")

        logger.info("Database connection established successfully")

        return connection
    
    except sqlite3.Error as error:
        logger.error("Database connection failed: %s", error)
        raise

def create_tables(connection):
    """
    Create database tables using the SQL schema file.

    Args:
        connection (sqlite3.Connection): SQLite database connection.
    """

    try:
        with open(SQL_SCHEMA_PATH, "r", encoding="utf-8") as file:
            sql_script = file.read()

        connection.executescript(sql_script)
        connection.commit()

        logger.info("Database tables created successfully.")

    except FileNotFoundError as error:
        logger.error("SQL schema file not found: %s", error)
        raise

    except sqlite3.Error as error:
        logger.error("Failed to create database tables: %s", error)
        raise

def load_location_dimension(connection, df):
    """
    Load location data into dim_location.

    Args:
        connection (sqlite3.Connection): SQLite database connection.
        df (pandas.DataFrame): Validate weather data.
    """

    location = df[
        ["location_name", "latitude", "longitude", "timezone"]
    ].drop_duplicates()

    insert_query = """
        INSERT OR IGNORE INTO dim_location (
            location_name,
            latitude,
            longitude,
            timezone
        )
        VALUES (?, ?, ?, ?);
    """

    for _, row in location.iterrows():
        connection.execute(
            insert_query,
            (
                row["location_name"],
                row["latitude"],
                row["longitude"],
                row["timezone"],
            ),
        )
    
    connection.commit()

    logger.info("Location dimension loaded successfully.")

def load_date_dimension(connection, df):
    """
    Load data data into dim_date.

    Args:
        connection (sqlite.Connection): SQLite database connection.
        df (pandas.DataFrame): Validated weather data.
    """

    unique_dates = df[["date"]].drop_duplicates()

    insert_query = """
        INSERT OR IGNORE INTO dim_date (
            full_date,
            day,
            month,
            year
        )
        VALUES (?, ?, ?, ?);
    """

    for _,row in unique_dates.iterrows():
        date_value = pd.to_datetime(row["date"])

        connection.execute(
            insert_query,
            (
                str(date_value.date()),
                int(date_value.day),
                int(date_value.month),
                int(date_value.year),
            )
        )

    connection.commit()

    logger.info("Date dimesion loaded successfully.")

def load_time_dimension(connection, df):
    """
    Load hour data into dim_time.

    Args:
        connection (sqlite3.Connection): SQLite database connection.
        df (pandas.DataFrame): Validate weather data.
    """

    unique_hours = df[["hour"]].drop_duplicates()

    insert_query = """
        INSERT OR IGNORE INTO dim_time (hour)
        VALUES (?);
    """

    for _,row in unique_hours.iterrows():
        connection.execute(
            insert_query,
            (int(row["hour"]),),
        )

    connection.commit()

    logger.info("Time dimension loaded successfully.")

def get_location_id(connection, location_name, latitude, longitude):
    """
    Get location_id from dim_location.

    Args:
        connection (sqlite3.Connection): SQLite database connection.
        location_name (str): Location name.
        latitude (float): Latitude.
        longitude (float): Longitude.

    Returns:
        int: location: location_id
    """

    query = """
        SELECT location_id
        FROM dim_location
        WHERE location_name = ?
            AND latitude = ?
            AND LONFITUDE = ?;
    """

    result = connection.execute(
        query,
        (location_name, latitude, longitude),
    ).fetchone()

    return result[0]