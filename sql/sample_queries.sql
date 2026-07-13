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
        ON fw.locaion_id = dl.location_id
    JOIN dim_date dd
        ON fw.date_id = dd.date_id
    JOIN dim_date dt
        ON fw.time_id = dt.time_id
    ORDER BY fw.observation_time;


-- 2 Average temperature by location
SELECT
    dl.location_name,
    ROUND(AVG(fw.temperature_celsius), 2) AS avg_temperature_celsius
FROM fact_weather fw
JOIN dim_location dl
     ON fw.location_id = dl.locaion_id
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
GROUP BY dl.locaion_name, dd.full_name
ORDER BY dd.full_date;

-- 4. Total precipitation by date
SELECT
    dl.location_name,
    dd.full_name,
    ROUND(SUM(fw.precipitation_nm), 2) AS total_precipitation_nm
FROM fact_weather fw
JOIN dim_location dl
    ON fw.location_id = dl.dim_location
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
ORDER BY dt.hour
