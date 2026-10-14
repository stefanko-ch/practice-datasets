# Zurich – hourly weather, 2009–2026

Hourly historical weather for the city of Zurich (lat 47.3769, lon 8.5417) from the Open-Meteo archive API, local time Europe/Zurich.

| | |
|---|---|
| Download | [`zurich_weather_hourly.csv`](https://github.com/stefanko-ch/practice-datasets/releases/download/v1/zurich_weather_hourly.csv) (6.8 MB) |
| Rows | 155,832 |
| Source | [https://open-meteo.com/en/docs/historical-weather-api](https://open-meteo.com/en/docs/historical-weather-api) |
| License | CC BY 4.0 (Open-Meteo) |

## Columns

| Column | Meaning |
|---|---|
| `time` | Start of the hour, local time |
| `temperature_c` | Air temperature 2 m, °C |
| `precipitation_mm` | Precipitation, mm |
| `rain_mm` | Rain, mm |
| `snowfall_cm` | Snowfall, cm |
| `wind_speed_kmh` | Wind speed 10 m, km/h |
| `cloud_cover_pct` | Cloud cover, % |

## Sample

### Sample extract (first 10 rows)

| time | temperature_c | precipitation_mm | rain_mm | snowfall_cm | wind_speed_kmh | cloud_cover_pct |
|---|---|---|---|---|---|---|
| 2009-01-01T00:00 | -0.2 | 0.5 | 0.1 | 0.28 | 1.8 | 99 |
| 2009-01-01T01:00 | 0.0 | 0.3 | 0.1 | 0.14 | 1.8 | 90 |
| 2009-01-01T02:00 | -0.0 | 0.2 | 0.1 | 0.07 | 1.5 | 90 |
| 2009-01-01T03:00 | -0.3 | 0.3 | 0.1 | 0.14 | 1.9 | 83 |
| 2009-01-01T04:00 | -0.7 | 0.5 | 0.0 | 0.35 | 4.7 | 96 |
| 2009-01-01T05:00 | -1.2 | 0.4 | 0.0 | 0.28 | 5.1 | 79 |
| 2009-01-01T06:00 | -1.6 | 0.2 | 0.0 | 0.14 | 5.9 | 59 |
| 2009-01-01T07:00 | -2.0 | 0.0 | 0.0 | 0.0 | 5.8 | 50 |
| 2009-01-01T08:00 | -2.9 | 0.0 | 0.0 | 0.0 | 5.8 | 47 |
| 2009-01-01T09:00 | -0.6 | 0.0 | 0.0 | 0.0 | 4.3 | 51 |
