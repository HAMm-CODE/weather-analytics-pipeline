"""
weather_etl_dag.py

Airflow DAG for running the Weather Analytics ETL pipeline daily.
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

from airflow import DAG 
from airflow.operators.python import PythonOperator


# Add the project root folder to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))


from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from src.load import load_weather_data