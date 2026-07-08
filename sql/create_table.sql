-- create_tables.sql
-- SQL schema for the Weather Analytics ETL project

-- Dimension table: stores location information 
CREATE TABLE IF NOT EXISTS dim_location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    timezone TEXT,
    UNIQUE(location_name, latitude, longitude)
);

CREATE TABLE IF NOT EXISTS dim_date(
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE NOT NULL UNIQUE,
    day INTEGER NOT NULL,
    month INTGER NOT NULL,
    year INTEGER NOT NULL
);

