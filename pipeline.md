                    ┌─────────────────┐
                    │  Open-Meteo API │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────┐
                  │ Extract Module   │
                  │ (extract.py)     │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Raw JSON Data    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Transform Module │
                  │ (transform.py)   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Validation Layer │
                  │ (validate.py)    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Load Module      │
                  │ (load.py)        │
                  └────────┬─────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ SQLite Database    │
                 │ weather.db         │
                 └────────┬───────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Star Schema           │
               │                       │
               │ dim_location          │
               │ dim_date              │
               │ dim_time              │
               │ fact_weather          │
               └───────────┬───────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Apache Airflow     │
                │ DAG Orchestration  │
                └────────────────────┘