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
    