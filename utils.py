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