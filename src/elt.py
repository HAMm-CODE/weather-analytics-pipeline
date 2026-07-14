"""
elt.py

Implements a simple ELT workflow for the Weather Analytics project.

ELT flow:
1. Extract raw weather data from Open-Meteo API
2. Load raw JSON into the staging table
3. Read raw data from staging
4. Transform the staged raw data
5. Validate the transformed data
6. Load the clean data into the final star schema
"""

import json
import logging
import sqlite3
