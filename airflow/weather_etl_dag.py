"""
weather_etl_dag.py

Airflow DAG for running the Weather Analytics ETL pipeline daily.
"""

import sys
from pathlib import path
from datetime import datetime, timedelta

