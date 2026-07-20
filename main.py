"""
main.py

Entry point running the weather ETL project manually
"""

import logging

from src.pipeline import WeatherETLPipeline
from src.utils import setup_logging

if __name__ == "__main__":
    setup_logging()

    pipeline = WeatherETLPipeline()
    pipeline.run()

    print("ETL pipeline completed successfully!")