"""
main_elt.py

Entry point for running the Weather Analytics ELT workflow manually.
"""

from src.elt import WeatherELTWorkflow
from src.utils import setup_logging


if __name__ == "__main__":
    setup_logging()

    workflow = WeatherELTWorkflow()
    workflow.run()

    print("Weather ELT workflow completed successfully!")