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

-- Dimension table: stores date information
CREATE TABLE IF NOT EXISTS dim_date(
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE NOT NULL UNIQUE,
    day INTEGER NOT NULL,
    month INTGER NOT NULL,
    year INTEGER NOT NULL
);

-- Dimension table: stores time/hour information
CREATE TABLE IF NOT EXISTS dim_time(
    time_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hour INTEGER NOT UNIQUE
);

-- Fact table: stores weather measurements
CREATE TABLE IF NOT EXISTS fact_weather (
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    time_id INTEGER NOT NULL,
    observation_time TIMESTAMP NOT NULL,
    temperature_celsius REAL,
    humidity_percent REAL,
    precipitation_nm REAL,
    wind_speed_kmh REAL,

    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),

    UNIQUE(location_id, observation_time)
);



