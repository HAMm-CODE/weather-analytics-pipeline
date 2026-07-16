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


default_args = {
    "owner": "Hamza",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def extract_task(**context):
    """
    Extract weather data from the Open-Meteo API.
    """

    raw_data = extract_weather_data()

    context["ti"].xcom_push(
        key="raw_weather_data",
        value=raw_data,
    )


def transform_task(**context):
    """
    Transform raw weather data into a clean tabular format.
    """

    raw_data = context["ti"].xcom_pull(
        task_ids="extract_weather_data",
        key="raw_weather_data",
    )

    clean_data = transform_weather_data(raw_data)

    # Convert DataFrame to JSON so Airflow can pass it between tasks
    clean_data_json = clean_data.to_json(
        orient="records",
        date_format="iso",
    )

    context["ti"].xcom_push(
        key="clean_weather_data",
        value=clean_data_json,
    )


def validate_task(**context):
    """
    Validate transformed weather data.
    """

    import pandas as pd

    clean_data_json = context["ti"].xcom_pull(
        task_ids="transform_weather_data",
        key="clean_weather_data",
    )

    clean_data = pd.read_json(clean_data_json)

    validated_data = validate_weather_data(clean_data)

    validated_data_json = validated_data.to_json(
        orient="records",
        date_format="iso",
    )

    context["ti"].xcom_push(
        key="validated_weather_data",
        value=validated_data_json,
    )


def load_task(**context):
    """
    Load validated weather data into the SQL star schema.
    """

    import pandas as pd

    validated_data_json = context["ti"].xcom_pull(
        task_ids="validate_weather_data",
        key="validated_weather_data",
    )

    validated_data = pd.read_json(validated_data_json)

    load_weather_data(validated_data)


with DAG(
    dag_id="weather_analytics_etl_pipeline",
    default_args=default_args,
    description="Daily ETL pipeline for Open-Meteo weather analytics",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["weather", "etl", "data-engineering"],
) as dag:

    extract = PythonOperator(
        task_id="extract_weather_data",
        python_callable=extract_task,
    )

    transform = PythonOperator(
        task_id="transform_weather_data",
        python_callable=transform_task,
    )

    validate = PythonOperator(
        task_id="validate_weather_data",
        python_callable=validate_task,
    )

    load = PythonOperator(
        task_id="load_weather_data",
        python_callable=load_task,
    )

    extract >> transform >> validate >> load