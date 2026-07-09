"""
main.py

Entry point running the weather ETL project manually
"""

import logging

from src.pipeline import WeatherETLPipeline


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler(),
    ],
)

if __name__ == "__main__":
    pipeline = WeatherETLPipeline()
    pipeline.run()

    print("ETL pipeline completed successfully!")