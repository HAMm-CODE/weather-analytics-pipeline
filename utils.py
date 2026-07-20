"""
utils.py

Utility/helper functions for the weather Analytics ETL project.
"""


import logging
from pathlib import Path

def create_project_folders():
    """
    Create required project folders if they do not exist.

    This prevents errors when writing logs or creating the SQLite database.
    """

    folders = [
        "data",
        "logs",
    ]

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)


def setup_logging():
    """
    Configure logging for the project.

    logs will be written to:
    - terminal
    - logs/pipeline.log
    """

    create_project_folders()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler(),
        ],
    )