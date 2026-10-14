# Zurich – automatic bike and pedestrian counts, 2009–2026

Counts of bikes and pedestrians at the automatic counting stations of the City of Zurich, in 15-minute intervals since 2009. Stations count bikes, pedestrians or both, in two directions. The number of active stations changes over the years – compare averages per station, not totals.

| | |
|---|---|
| Download | [`zurich_bike_pedestrian_counts.parquet`](https://github.com/stefanko-ch/practice-datasets/releases/download/v1/zurich_bike_pedestrian_counts.parquet) (61.4 MB) |
| Rows | 15,764,613 |
| Source | [https://data.stadt-zuerich.ch/dataset/ted_taz_verkehrszaehlungen_werte_fussgaenger_velo](https://data.stadt-zuerich.ch/dataset/ted_taz_verkehrszaehlungen_werte_fussgaenger_velo) |
| License | CC0 (Open Data City of Zurich) |

## Columns

| Column | Meaning |
|---|---|
| `FK_STANDORT` | Station ID (→ zurich-bike-pedestrian-stations, column `station_id`) |
| `DATUM` | Start of the 15-minute interval, local time, text `yyyy-MM-ddTHH:mm` |
| `VELO_IN / VELO_OUT` | Bikes in direction in / out (NULL if the station does not count bikes) |
| `FUSS_IN / FUSS_OUT` | Pedestrians in direction in / out (NULL if the station does not count pedestrians) |
| `OST / NORD` | Station coordinates, Swiss LV95 |

## Sample

### Sample extract (first 10 rows)

| FK_STANDORT | DATUM | VELO_IN | VELO_OUT | FUSS_IN | FUSS_OUT | OST | NORD |
|---|---|---|---|---|---|---|---|
| 5 | 2009-12-02T00:00 | 2 | 3 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T00:15 | 0 | 2 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T00:30 | 0 | 0 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T00:45 | 0 | 2 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T01:00 | 0 | 0 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T01:15 | 0 | 1 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T01:30 | 0 | 1 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T01:45 | 0 | 0 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T02:00 | 1 | 0 |  |  | 2682933 | 1248821 |
| 5 | 2009-12-02T02:15 | 0 | 0 |  |  | 2682933 | 1248821 |
