"""Build the release assets and the dataset documentation.

    uv run --with pandas --with pyarrow --with openpyxl scripts/build_release.py

- reads the local raw files in data/ (gitignored)
- writes one release asset per dataset to dist/ (single files as they are, multi-file datasets as ZIP)
- writes datasets/<name>/README.md (description, columns, sample extract) and datasets/<name>/sample.* (first rows)
- rewrites the catalog table in README.md between the CATALOG markers
"""
import json
import pathlib
import re
import shutil
import zipfile

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, DIST, DOCS = ROOT / "data", ROOT / "dist", ROOT / "datasets"
RELEASE = "v1"
URL = f"https://github.com/stefanko-ch/practice-datasets/releases/download/{RELEASE}"

CC0_ZH = "CC0 (Open Data City of Zurich)"
DATASETS = [
    dict(
        name="zurich-bike-pedestrian-counts", asset="zurich_bike_pedestrian_counts.parquet",
        files=["mobility/bike_pedestrian_counts/verkehrszaehlungen_werte_fussgaenger_velo_alle_jahre.parquet"],
        title="Zurich – automatic bike and pedestrian counts, 2009–2026",
        description="Counts of bikes and pedestrians at the automatic counting stations of the City of Zurich, "
                    "in 15-minute intervals since 2009. Stations count bikes, pedestrians or both, in two directions. "
                    "The number of active stations changes over the years – compare averages per station, not totals.",
        source="https://data.stadt-zuerich.ch/dataset/ted_taz_verkehrszaehlungen_werte_fussgaenger_velo", license=CC0_ZH,
        columns={"FK_STANDORT": "Station ID (→ zurich-bike-pedestrian-stations, column `station_id`)",
                 "DATUM": "Start of the 15-minute interval, local time, text `yyyy-MM-ddTHH:mm`",
                 "VELO_IN / VELO_OUT": "Bikes in direction in / out (NULL if the station does not count bikes)",
                 "FUSS_IN / FUSS_OUT": "Pedestrians in direction in / out (NULL if the station does not count pedestrians)",
                 "OST / NORD": "Station coordinates, Swiss LV95"},
    ),
    dict(
        name="zurich-bike-pedestrian-counts-2025", asset="zurich_bike_pedestrian_counts_2025.csv",
        files=["sample_data/csv/2025_verkehrszaehlungen_werte_fussgaenger_velo.csv"],
        title="Zurich – bike and pedestrian counts 2025 only (CSV)",
        description="The year 2025 of `zurich-bike-pedestrian-counts` as a single CSV file – handy for CSV-reading and "
                    "window-function exercises. Same columns as the Parquet dataset.",
        source="https://data.stadt-zuerich.ch/dataset/ted_taz_verkehrszaehlungen_werte_fussgaenger_velo", license=CC0_ZH,
    ),
    dict(
        name="zurich-bike-pedestrian-stations", asset="zurich_bike_pedestrian_stations.csv",
        files=["mobility/bike_pedestrian_stations/standorte_fuss_velo_zaehlstellen.csv"],
        title="Zurich – bike and pedestrian counting stations",
        description="All 175 automatic bike/pedestrian counting stations (current and former) with name, directions, "
                    "operating period and WGS84 coordinates. Exported from the City of Zurich WFS service.",
        source="https://data.stadt-zuerich.ch/dataset/geo_standorte_der_automatischen_fuss__und_velozaehlungen", license=CC0_ZH,
        columns={"station_id": "Station ID (= `FK_STANDORT` in the counts)", "abkuerzung": "Short code",
                 "bezeichnung": "Station name", "velo / fuss": "1 if the station counts bikes / pedestrians",
                 "richtung_in / richtung_out": "Meaning of direction in / out", "status": "`aktuell` (active) or `früher` (former)",
                 "von / bis": "Operating period", "korrekturfaktor": "Correction factor of the counting device",
                 "lon / lat": "WGS84 coordinates"},
    ),
    dict(
        name="zurich-motorized-traffic-counts", asset="zurich_motorized_traffic_counts.parquet",
        files=["mobility/motorized_traffic_counts/sid_dav_verkehrszaehlung_miv_od2031_alle_jahre.parquet"],
        title="Zurich – motorized traffic counts, 2012–2026",
        description="Hourly counts of motor vehicles at ≈ 110 counting sites of the City of Zurich since 2012, one row per "
                    "measuring point (site × direction) and hour. Includes site names, axes and LV95 coordinates.",
        source="https://data.stadt-zuerich.ch/dataset/sid_dav_verkehrszaehlung_miv_od2031", license=CC0_ZH,
        columns={"MSID / MSName": "Measuring point (one direction of a site)", "ZSID / ZSName": "Counting site",
                 "Achse": "Street", "EKoord / NKoord": "Coordinates, Swiss LV95", "Richtung": "`einwärts` (into the city) / `auswärts`",
                 "MessungDatZeit": "Start of the hour incl. time zone, text", "AnzFahrzeuge": "Number of vehicles",
                 "AnzFahrzeugeStatus": "`Gemessen` (measured), `Imputiert` (estimated), `Fehlend` (missing)"},
    ),
    dict(
        name="zurich-weather-hourly", asset="zurich_weather_hourly.csv",
        files=["mobility/weather/weather_zurich_hourly_2009_2026.csv"],
        title="Zurich – hourly weather, 2009–2026",
        description="Hourly historical weather for the city of Zurich (lat 47.3769, lon 8.5417) from the Open-Meteo archive API, "
                    "local time Europe/Zurich.",
        source="https://open-meteo.com/en/docs/historical-weather-api", license="CC BY 4.0 (Open-Meteo)",
        columns={"time": "Start of the hour, local time", "temperature_c": "Air temperature 2 m, °C",
                 "precipitation_mm": "Precipitation, mm", "rain_mm": "Rain, mm", "snowfall_cm": "Snowfall, cm",
                 "wind_speed_kmh": "Wind speed 10 m, km/h", "cloud_cover_pct": "Cloud cover, %"},
    ),
    dict(
        name="basel-population", asset="basel_population.parquet",
        files=["sample_data/parquet/Kanton_BS_Wohnbevoelkerung_nach_Geschlecht_Staatsangehoerigkeit_und_Wohnviertel.parquet"],
        title="Basel-Stadt – resident population by sex, nationality and neighbourhood",
        description="Resident population of the canton of Basel-Stadt per year, municipality, neighbourhood, sex and nationality.",
        source="https://data.bs.ch/explore/dataset/100126/", license="CC BY 4.0 (Open Data Basel-Stadt)",
    ),
    dict(
        name="adventureworks", asset="adventureworks.zip", zip_dir="adventureworks",
        title="AdventureWorks – sales database of a bike manufacturer (11 tables)",
        description="The classic Microsoft sample database as CSV files `<Schema>.<Table>.csv`: persons, addresses, "
                    "products and categories, customers, sales orders and order lines, sales territories. "
                    "Ideal for JOINs, aggregations and star-schema exercises.",
        source="https://github.com/microsoft/sql-server-samples", license="MIT (Microsoft sql-server-samples)",
        sample_file="Production.Product.csv",
    ),
    dict(
        name="world-countries-states-cities", asset="world_countries_states_cities.zip", zip_dir="sample_data",
        zip_members=["csv/countries.csv", "csv/states.csv", "csv/cities.csv", "json/countries.json", "json/states.json",
                     "xml/countries.xml", "xml/states.xml", "yml/countries.yml", "yml/states.yml"],
        title="World – countries, states and cities in CSV, JSON, XML and YAML",
        description="250 countries, 5 000 states and 150 000 cities – the same data in four formats, for file-format exercises. "
                    "Folders `csv/`, `json/`, `xml/`, `yml/`.",
        source="https://github.com/dr5hn/countries-states-cities-database", license="ODbL 1.0",
        sample_file="csv/countries.csv",
    ),
    dict(
        name="travel-offers", asset="travel_offers.json", files=["synthetic/travel_offers.json"],
        title="Travel offers – nested JSON (synthetic)",
        description="5 000 package-holiday offers to Cyprus in a deeply nested JSON structure (`root.Page[].Position…`): "
                    "hotel, destination, package, price. Typical of web/API exports – needs `explode` and dot notation. "
                    "Hotels and tour operators are fictional, places are real.",
        source="Synthetic – generated by `scripts/generate_synthetic.py`", license="CC0",
    ),
    dict(
        name="financials-sample", asset="financials_sample.xlsx", files=["synthetic/financials_sample.xlsx"],
        title="Financials – Excel workbook with two sheets (synthetic)",
        description="Sheet `Financials1`: monthly budget/actuals per account and business unit (wide format, Jan–Dec). "
                    "Sheet `Financials2`: 700 sales transactions. Deliberately messy like real exports: the header typo "
                    "`Businees Unit`, the column ` Sales` with a leading space, the year stored as text.",
        source="Synthetic – generated by `scripts/generate_synthetic.py`", license="CC0",
    ),
    dict(
        name="wine", asset="wine.csv", files=["sample_data/csv/WineQuality.csv"],
        title="Wine – chemical analysis of 178 Italian wines (UCI Wine)",
        description="13 chemical measurements of wines from three cultivars (column `Quality` = cultivar class 0–2). "
                    "Note: this is the UCI *Wine* dataset, not *Wine Quality*.",
        source="https://archive.ics.uci.edu/dataset/109/wine", license="CC BY 4.0 (UCI Machine Learning Repository)",
    ),
    dict(
        name="diamonds", asset="diamonds.csv", files=["sample_data/csv/diamonds.csv"],
        title="Diamonds – prices and attributes of ≈ 54 000 diamonds",
        description="Carat, cut, colour, clarity, dimensions and price. First column is an unnamed row index.",
        source="https://ggplot2.tidyverse.org/reference/diamonds.html", license="MIT (ggplot2)",
    ),
    dict(
        name="hr-employees", asset="hr_employees.csv", files=["synthetic/hr_employees.csv"],
        title="HR – employee satisfaction and attrition (synthetic)",
        description="15 000 employees with satisfaction, evaluation, projects, working hours, department, salary band and "
                    "whether they left. Header quirks on purpose: `average_montly_hours`, `Departments`.",
        source="Synthetic – generated by `scripts/generate_synthetic.py`", license="CC0",
    ),
    dict(
        name="personality", asset="personality.csv", files=["synthetic/personality.csv"],
        title="Personality – introvert vs. extrovert behaviour (synthetic)",
        description="2 900 persons with social behaviour indicators and the label `Personality`; ≈ 2 % missing values.",
        source="Synthetic – generated by `scripts/generate_synthetic.py`", license="CC0",
    ),
    dict(
        name="small-tables", asset="small_tables.zip", zip_dir="sample_data/csv",
        zip_members=["weather_timeseries.csv", "blog_posts.csv", "product_reviews.csv", "popular_currency_rate_dollar.csv"],
        title="Small tables for SQL and text exercises (synthetic)",
        description="Four tiny tables: daily weather of a few cities, blog posts, product reviews, currency rates "
                    "(Unix timestamps).", source="Synthetic, written for teaching", license="CC0", sample_file="weather_timeseries.csv",
    ),
    dict(
        name="documents", asset="documents.zip", zip_dir="sample_data",
        zip_members=["pdf/employee_data.pdf", "txt/sample_text.txt", "txt/numbered_sample_text.txt"],
        title="Documents for parsing exercises (synthetic)",
        description="A two-page PDF with a fictional employee directory and two small text files.",
        source="Synthetic, written for teaching", license="CC0",
    ),
]


def read_table(path: pathlib.Path) -> pd.DataFrame:
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    if path.suffix == ".csv":
        return pd.read_csv(path, low_memory=False)
    if path.suffix == ".xlsx":
        return pd.read_excel(path, sheet_name=0)
    raise ValueError(path)


def md_table(df: pd.DataFrame) -> str:
    cell = (lambda v: "" if pd.isna(v) else str(v).replace("|", "\\|")[:40])
    lines = ["| " + " | ".join(map(str, df.columns)) + " |", "|" + "---|" * len(df.columns)]
    lines += ["| " + " | ".join(cell(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(lines)


DIST.mkdir(exist_ok=True)
catalog = []
for d in DATASETS:
    out_dir = DOCS / d["name"]
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True)
    asset = DIST / d["asset"]
    rows, sample_md = None, ""

    if d["asset"].endswith(".zip"):
        base = DATA / d["zip_dir"]
        members = d.get("zip_members") or sorted(p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file() and p.name != ".DS_Store")
        with zipfile.ZipFile(asset, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for m in members:
                zf.write(base / m, m)
        listing = []
        for m in members:
            p = base / m
            n = f"{len(read_table(p)):,} rows" if p.suffix == ".csv" else f"{p.stat().st_size / 1e3:,.0f} KB"
            listing.append(f"| `{m}` | {n} |")
        sample_md = "### Files in the ZIP\n\n| File | Size |\n|---|---|\n" + "\n".join(listing) + "\n\n"
        if d.get("sample_file"):
            df = read_table(base / d["sample_file"])
            df.head(100).to_csv(out_dir / "sample.csv", index=False)
            sample_md += f"### Sample extract of `{d['sample_file']}` (first 10 rows)\n\n{md_table(df.head(10))}\n"
    else:
        src = DATA / d["files"][0]
        shutil.copyfile(src, asset)
        if src.suffix == ".json":
            data = json.loads(src.read_text())
            (out_dir / "sample.json").write_text(json.dumps({"root": {"Page": data["root"]["Page"][:2]}}, ensure_ascii=False, indent=1))
            rows = len(data["root"]["Page"])
            sample_md = f"### Sample extract\n\nThe first two offers: [sample.json](sample.json)\n"
        elif src.suffix == ".xlsx":
            parts = []
            for sheet in ("Financials1", "Financials2"):
                df = pd.read_excel(src, sheet_name=sheet)
                df.head(100).to_csv(out_dir / f"sample_{sheet}.csv", index=False)
                parts.append(f"### Sample extract of sheet `{sheet}` ({len(df):,} rows, first 5)\n\n{md_table(df.head(5))}\n")
            sample_md = "\n".join(parts)
        else:
            df = read_table(src)
            rows = len(df)
            df.head(100).to_csv(out_dir / "sample.csv", index=False)
            sample_md = f"### Sample extract (first 10 rows)\n\n{md_table(df.head(10))}\n"

    b = asset.stat().st_size
    size = f"{b / 1e6:,.1f} MB" if b >= 1e6 else f"{b / 1e3:,.0f} KB"
    cols = ""
    if d.get("columns"):
        cols = "## Columns\n\n| Column | Meaning |\n|---|---|\n" + "\n".join(f"| `{k}` | {v} |" for k, v in d["columns"].items()) + "\n\n"
    rows_txt = f"{rows:,}" if rows else "see below"
    source_md = f"[{d['source']}]({d['source']})" if d["source"].startswith("http") else d["source"]
    (out_dir / "README.md").write_text(
        f"# {d['title']}\n\n{d['description']}\n\n"
        f"| | |\n|---|---|\n| Download | [`{d['asset']}`]({URL}/{d['asset']}) ({size}) |\n| Rows | {rows_txt} |\n"
        f"| Source | {source_md} |\n"
        f"| License | {d['license']} |\n\n{cols}## Sample\n\n{sample_md}"
    )
    catalog.append(f"| [{d['name']}](datasets/{d['name']}/) | {d['title']} | `{d['asset']}` | {size} | {d['license']} |")
    print(f"{d['asset']:<42} {size:>9}")

readme = (ROOT / "README.md").read_text()
table = "| Dataset | Content | Release asset | Size | License |\n|---|---|---|---|---|\n" + "\n".join(catalog)
readme = re.sub(r"<!-- CATALOG -->.*<!-- /CATALOG -->", f"<!-- CATALOG -->\n{table}\n<!-- /CATALOG -->", readme, flags=re.S)
(ROOT / "README.md").write_text(readme)
