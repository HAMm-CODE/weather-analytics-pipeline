--sample_queries.sql
--sample analytics queries for the weather Analytics ETL project

--1. View all weather records with location, date, and time details
    SELECT
        fw.weather_id,
        dl.location_name,
        dl.latitude,
        dl.longitude,
        dd.full_date,
        dt.hour,
        fw.observation_time,
        fw.humidity_percent,
        fw.precipitation_nm,
        fw.wind_speed_kmh
    FROM fact_weather fw
    JOIN dim_location dl
        ON fw.location_id = dl.location_id
    JOIN dim_date dd
        ON fw.date_id = dd.date_id
    JOIN dim_time dt
        ON fw.time_id = dt.time_id
    ORDER BY fw.observation_time;


-- 2 Average temperature by location
SELECT
    dl.location_name,
    ROUND(AVG(fw.temperature_celsius), 2) AS avg_temperature_celsius
FROM fact_weather fw
JOIN dim_location dl
     ON fw.location_id = dl.location_id
GROUP BY dl.location_name;

-- 3. Minimum and maximum temperature by date
SELECT
    dl.location_name,
    dd.full_date,
    ROUND(MIN(fw.temperature_celsius), 2) AS min_temperature_celsius,
    ROUND(MAX(fw.temperature_celsius), 2) AS max_temperature_celsius
FROM fact_weather fw
JOIN dim_location dl
    ON fw.location_id = dl.location_id
JOIN dim_date dd
    ON fw.date_id = dd.date_id
GROUP BY dl.location_name, dd.full_date
ORDER BY dd.full_date;

-- 4. Total precipitation by date
SELECT
    dl.location_name,
    dd.full_date,
    ROUND(SUM(fw.precipitation_nm), 2) AS total_precipitation_nm
FROM fact_weather fw
JOIN dim_location dl
    ON fw.location_id = dl.location_id
JOIN dim_date dd
    ON fw.date_id = dd.date_id
GROUP BY dl.location_name, dd.full_date
ORDER by dd.full_date;

-- 5. Average humidity by hour
SELECT
    dt.hour,
    ROUND(AVG(fw.humidity_percent), 2) AS avg_humidity_percent
FROM fact_weather fw
JOIN dim_time dt
    ON fw.time_id = dt.time_id
GROUP BY dt.hour
ORDER BY dt.hour;

-- 6. Average wind speed by hour
SELECT
    dt.hour,
    ROUND(AVG(fw.wind_speed_kmh), 2) AS avg_wind_speed_kmh
FROM fact_weather fw
JOIN dim_time dt
    ON fw.time_id = dt.time_id
GROUP BY dt.hour
ORDER BY dt.hour;

-- 7. Hottest recorded hour
SELECT
    dl.location_name,
    dd.full_date,
    dt.hour,
    fw.temperature_celsius
FROM fact_weather fw
JOIN dim_location dl
    ON fw.location_id = dl.location_id
JOIN dim_date dd
    ON fw.date_id = dd.date_id
JOIN dim_time dt
    ON fw.time_id = dt.time_id
ORDER BY fw.temperature_celsius DESC
LIMIT 1;

-- 8. Coldest recorded hour
SELECT
    dl.location_name,
    dd.full_date,
    dt.hour,
    fw.temperature_celsius
FROM fact_weather fw
JOIN dim_location dl
    ON fw.location_id = dl.location_id
JOIN dim_date dd
    ON fw.date_id = dd.date_id
JOIN dim_time dt
    ON fw.time_id = dt.time_id
ORDER BY fw.temperature_celsius ASC
LIMIT 1;

-- 9. Count number of records loaded into fact table
SELECT
    COUNT(*) AS total_weather_records
FROM fact_weather;

-- 10. Check records in each dimension table
SELECT 'dim_location' AS table_name, COUNT(*) AS total_records
FROM dim_location

UNION ALL 

SELECT 'dim_date' AS table_name, COUNT(*) AS total_records
FROM dim_date

UNION ALL

SELECT 'dim_time' AS table_name, COUNT(*) AS total_records
FROM dim_time

UNION ALL

SELECT 'fact_weather' AS table_name, COUNT(*) AS total_records
FROM fact_weather;

-- 11. View raw records loaded into the staging table
SELECT
    raw_id,
    location_name,
    latitude,
    longitude,
    timezone,
    loaded_at
FROM stg_weather_raw
ORDER BY raw_id DESC;