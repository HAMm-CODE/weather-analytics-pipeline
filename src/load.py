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