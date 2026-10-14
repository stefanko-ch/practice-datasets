# Zurich – bike and pedestrian counting stations

All 175 automatic bike/pedestrian counting stations (current and former) with name, directions, operating period and WGS84 coordinates. Exported from the City of Zurich WFS service.

| | |
|---|---|
| Download | [`zurich_bike_pedestrian_stations.csv`](https://github.com/stefanko-ch/practice-datasets/releases/download/v1/zurich_bike_pedestrian_stations.csv) (20 KB) |
| Rows | 175 |
| Source | [https://data.stadt-zuerich.ch/dataset/geo_standorte_der_automatischen_fuss__und_velozaehlungen](https://data.stadt-zuerich.ch/dataset/geo_standorte_der_automatischen_fuss__und_velozaehlungen) |
| License | CC0 (Open Data City of Zurich) |

## Columns

| Column | Meaning |
|---|---|
| `station_id` | Station ID (= `FK_STANDORT` in the counts) |
| `abkuerzung` | Short code |
| `bezeichnung` | Station name |
| `velo / fuss` | 1 if the station counts bikes / pedestrians |
| `richtung_in / richtung_out` | Meaning of direction in / out |
| `status` | `aktuell` (active) or `früher` (former) |
| `von / bis` | Operating period |
| `korrekturfaktor` | Correction factor of the counting device |
| `lon / lat` | WGS84 coordinates |

## Sample

### Sample extract (first 10 rows)

| station_id | abkuerzung | bezeichnung | velo | fuss | richtung_in | richtung_out | status | von | bis | korrekturfaktor | lon | lat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FZS_HARD | Hardeggsteg | 0 | 1 | Kloster-Fahr-Weg | Hardturmstrasse | früher | 2015-10-01 | 2016-03-31 | 0.86 | 8.504128 | 47.395281 |
| 2 | FZS_ALTO | Altstetterstrasse Ost | 0 | 1 | Bhf. Altstetten | Lindenplatz | früher | 2015-10-01 | 2020-08-24 | 1.02 | 8.487502 | 47.39099 |
| 3 | FZS_LETD | Letten / Dynamo | 0 | 1 | Limmatplatz | Hauptbahnhof | früher | 2015-10-01 | 2016-03-29 | 0.89 | 8.537536 | 47.3843 |
| 4 | FZS_ZEHN | Zehntenhausplatz Unterführung | 0 | 1 | Louis Conne Weg | In Böden | früher | 2015-10-01 | 2016-03-31 | 0.95 | 8.506434 | 47.419105 |
| 5 | VZS_LUXG | Lux-Guyer-Weg | 1 | 0 | Innenstadt | Wipkingen | früher | 2009-12-02 | 2018-12-20 | 1.0 | 8.536954 | 47.384998 |
| 6 | VZS_MYTH | Mythenquai | 1 | 0 | Innenstadt | Wollishofen | früher | 2010-07-14 | 2018-12-21 | 1.2 | 8.535617 | 47.358655 |
| 7 | VZS_BINZ | Binzmühlestrasse | 1 | 0 | Oerlikon | Glaubtenstrasse | früher | 2010-11-30 | 2018-04-04 | 1.22 | 8.523286 | 47.413641 |
| 8 | VZS_SCHE | Scheuchzerstrasse | 1 | 0 | Innenstadt | Irchel | früher | 2010-09-23 | 2018-12-20 | 1.05 | 8.545377 | 47.382435 |
| 9 | VZS_ANDR | Andreasstrasse | 1 | 0 | Oerlikon | Wallisellen | früher | 2010-12-16 | 2019-03-13 | 1.14 | 8.559332 | 47.413081 |
| 10 | VZS_SIHL | Sihlpromenade | 1 | 0 | Innenstadt | Saalsporthalle | früher | 2010-07-14 | 2018-12-21 | 1.09 | 8.52924 | 47.369185 |
