                 dim_date
              ┌────────────┐
              │ date_id PK │
              │ date       │
              │ year       │
              │ month      │
              │ day        │
              └─────┬──────┘
                    │
                    │
┌──────────────┐    │    ┌──────────────┐
│ dim_location │    │    │   dim_time   │
│──────────────│    │    │──────────────│
│ location_id PK│   │    │ time_id PK   │
│ city         │    │    │ hour         │
│ latitude     │    │    │ minute       │
│ longitude    │    │    └──────┬───────┘
└──────┬────────┘    │           │
       │             │           │
       └─────────────┼───────────┘
                     │
              ┌──────▼────────┐
              │ fact_weather  │
              │───────────────│
              │ weather_id PK │
              │ location_id FK│
              │ date_id FK    │
              │ time_id FK    │
              │ temperature   │
              │ humidity      │
              │ wind_speed    │
              └───────────────┘