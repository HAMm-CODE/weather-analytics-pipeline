"""
load.py

Loads validated weather data into a SQLite database using a star schema.
"""

import logging
import sqlite3

import pandas as pd

from src.config import DATABASE_PATH, SQL_SCHEMA_PATH

logger = logging.getLogger(__name__)

