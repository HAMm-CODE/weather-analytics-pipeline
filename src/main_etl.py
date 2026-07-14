"""
main_elt.py

Entry point for running the Weather Analytics ELT workflow manually.
"""

import logging

from src.elt import WeatherELTWorkflow


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler(),
    ],
)
