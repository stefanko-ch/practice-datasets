# Zurich – motorized traffic counts, 2012–2026

Hourly counts of motor vehicles at ≈ 110 counting sites of the City of Zurich since 2012, one row per measuring point (site × direction) and hour. Includes site names, axes and LV95 coordinates.

| | |
|---|---|
| Download | [`zurich_motorized_traffic_counts.parquet`](https://github.com/stefanko-ch/practice-datasets/releases/download/v1/zurich_motorized_traffic_counts.parquet) (73.0 MB) |
| Rows | 23,446,586 |
| Source | [https://data.stadt-zuerich.ch/dataset/sid_dav_verkehrszaehlung_miv_od2031](https://data.stadt-zuerich.ch/dataset/sid_dav_verkehrszaehlung_miv_od2031) |
| License | CC0 (Open Data City of Zurich) |

## Columns

| Column | Meaning |
|---|---|
| `MSID / MSName` | Measuring point (one direction of a site) |
| `ZSID / ZSName` | Counting site |
| `Achse` | Street |
| `EKoord / NKoord` | Coordinates, Swiss LV95 |
| `Richtung` | `einwärts` (into the city) / `auswärts` |
| `MessungDatZeit` | Start of the hour incl. time zone, text |
| `AnzFahrzeuge` | Number of vehicles |
| `AnzFahrzeugeStatus` | `Gemessen` (measured), `Imputiert` (estimated), `Fehlend` (missing) |

## Sample

### Sample extract (first 10 rows)

| MSID | MSName | ZSID | ZSName | Achse | HNr | Hoehe | EKoord | NKoord | Richtung | Knummer | Kname | AnzDetektoren | D1ID | D2ID | D3ID | D4ID | MessungDatZeit | LieferDat | AnzFahrzeuge | AnzFahrzeugeStatus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T00:00:00+01:00 | 2021-02-03 |  | Fehlend |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T01:00:00+01:00 | 2021-02-03 | 256 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T02:00:00+01:00 | 2021-02-03 | 186 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T03:00:00+01:00 | 2021-02-03 | 142 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T04:00:00+01:00 | 2021-02-03 | 116 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T05:00:00+01:00 | 2021-02-03 | 67 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T06:00:00+01:00 | 2021-02-03 | 73 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T07:00:00+01:00 | 2021-02-03 | 43 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T08:00:00+01:00 | 2021-02-03 | 52 | Gemessen |
| Z001M001 | Unbekannt | Z001 | Seestrasse (Strandbad Wollishofen) | Seestrasse | 451 | Unbekannt | 2683009.89 | 1243936.2 | auswärts | 789 | Badanstalt Wollishofen | 1 | 2 | Unbekannt | Unbekannt | Unbekannt | 2012-01-01T09:00:00+01:00 | 2021-02-03 | 56 | Gemessen |
