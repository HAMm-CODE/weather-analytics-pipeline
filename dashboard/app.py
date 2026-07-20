"""
app.py

Streamlit dashboard for the Weather Analytics ETL project.
"""

import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st


DATABASE_PATH = Path("data/weather.db")


def load_weather_data():
    """
    Load weather data from the SQLite star schema.

    Returns:
        pandas.DataFrame: Weather analytics data.
    """

    query = """
        SELECT
            fw.weather_id,
            dl.location_name,
            dl.latitude,
            dl.longitude,
            dd.full_date,
            dt.hour,
            fw.observation_time,
            fw.temperature_celsius,
            fw.humidity_percent,
            fw.precipitation_mm,
            fw.wind_speed_kmh
        FROM fact_weather fw
        JOIN dim_location dl
            ON fw.location_id = dl.location_id
        JOIN dim_date dd
            ON fw.date_id = dd.date_id
        JOIN dim_time dt
            ON fw.time_id = dt.time_id
        ORDER BY fw.observation_time;
    """

    connection = sqlite3.connect(DATABASE_PATH)

    df = pd.read_sql_query(query, connection)

    connection.close()

    df["observation_time"] = pd.to_datetime(df["observation_time"])
    df["full_date"] = pd.to_datetime(df["full_date"])

    return df
