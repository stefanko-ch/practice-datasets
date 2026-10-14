"""Generate the synthetic datasets of this repo (deterministic, seed 42).

They replace files of unclear origin from earlier course material. Structure, column names, data types and the
deliberate quirks (typos in headers, leading spaces, numbers stored as text) are kept identical, so exercises written
for the old files keep working.

    uv run --with openpyxl scripts/generate_synthetic.py      # writes into data/synthetic/
"""
import datetime as dt
import json
import pathlib
import random

import openpyxl

random.seed(42)
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "synthetic"
OUT.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------- travel offers (nested JSON, root.Page[])
LOCATIONS = {  # real places in the Republic of Cyprus with approximate coordinates
    ("620", "Republik Zypern - Süden"): [
        ("572", "Ayia Napa", 34.986, 33.999), ("573", "Protaras", 35.012, 34.058),
        ("574", "Pernera - Kalamies Beach (Protaras)", 35.032, 34.061), ("575", "Pyla (Larnaca)", 34.954, 33.689),
        ("576", "Larnaca", 34.917, 33.629), ("577", "Limassol - Pareklisia", 34.723, 33.165),
    ],
    ("621", "Republik Zypern - Westen"): [
        ("580", "Paphos", 34.776, 32.424), ("581", "Paphos - Kissonerga", 34.818, 32.396),
        ("582", "Paphos - Chloraka", 34.802, 32.404), ("583", "Polis Chrysochous", 35.036, 32.426),
    ],
}
HOTEL_WORDS_A = ["Azure", "Coral", "Olive", "Sunset", "Lemon", "Harbour", "Aphrodite", "Cedar", "Pebble", "Marina", "Golden", "Sea Breeze"]
HOTEL_WORDS_B = ["Bay Resort", "Beach Hotel", "Gardens", "Suites", "Village", "Palace", "Apartments", "Boutique Hotel"]
OPERATORS = [("STA", "Sample Tours A"), ("STB", "Sample Tours B"), ("STC", "Sample Tours C"), ("STD", "Sample Tours D"), ("STE", "Sample Tours E")]
MEALS = [("FR", "Frühstück", 0.5), ("HP", "Halbpension", 0.3), ("AI", "All Inclusive", 0.15), ("AP", "All Inclusive Plus", 0.05)]

hotels = []
for i in range(46):
    (region, locs) = random.choice(list(LOCATIONS.items()))
    loc = random.choice(locs)
    name = f"{random.choice(HOTEL_WORDS_A)} {random.choice(HOTEL_WORDS_B)}"
    hotels.append(dict(id=str(9000 + i), giata=str(70000 + i), name=name, cls=random.choice(["3", "3,5", "4", "4,5", "5"]),
                       region=region, loc=loc, lat=loc[2] + random.uniform(-0.01, 0.01), lon=loc[3] + random.uniform(-0.01, 0.01),
                       rating=random.randint(60, 95)))

offers = []
updated = dt.datetime(2026, 2, 22, 1, 25, 38)
for _ in range(5000):
    h = random.choice(hotels)
    meal = random.choices(MEALS, weights=[m[2] for m in MEALS])[0]
    op = random.choice(OPERATORS)
    days = random.choice([5, 7, 7, 7, 10, 14])
    departure = dt.date(2026, 4, 1) + dt.timedelta(days=random.randint(0, 150))
    price = int(days * random.uniform(25, 60) * (1 + 0.25 * MEALS.index(meal)) * (0.8 + 0.1 * float(h["cls"].replace(",", "."))))
    offers.append({"Position": {
        "Updated": {"Unix": int(updated.timestamp()), "Value": updated.strftime("%d.%m.%Y %H:%M:%S")},
        "Type": "GenericPlatform Hotel",
        "Picture": f"https://images.example.com/hotels/{h['id']}.jpg",
        "Text-Line": ["", "", "", ""], "Extra": ["", "", "", ""],
        "Link": {"HRef": "", "OverrideState": False}, "LinkOffers": {"HRef": ""}, "LinkHotels": {"HRef": ""},
        "Duration": {"Measure": "Tage", "Value": days},
        "Price": {"Currency": "EUR", "Suffix": "p.P.", "Value": price},
        "Package": {
            "AdultsNumber": 2, "ChildrenCount": random.choice([0, 0, 0, 1, 2]),
            "DepartureDate": {"Format": "German", "Value": departure.strftime("%d.%m.%Y")},
            "TourOperator": {"Acronym": op[0], "Name": op[1]},
            "MealPlan": {"Acronym": meal[0], "Name": meal[1]},
            "RoomCode": random.choice(["DZ", "DZM", "SU", "AP"]),
            "RoomType": {"Acronym": "", "GlobalType": "", "Name": ""},
            "Hotelrating": {"Rating": str(h["rating"]), "Recommend": f"{h['rating'] - random.uniform(0, 10):.1f}%".replace(".", ","),
                            "Average": f"{h['rating'] / 16:.1f}".replace(".", ",")},
            "TravelType": "LAEN",
        },
        "Destination": {"Country": {"Id": "CY", "Name": "Zypern"},
                        "Region": {"Id": h["region"][0], "Name": h["region"][1]},
                        "Location": {"Id": h["loc"][0], "Name": h["loc"][1]}},
        "Hotel": {"Id": h["id"], "GiataId": h["giata"], "Name": h["name"], "Class": h["cls"],
                  "Lat": f"{h['lat']:.5f}", "Lon": f"{h['lon']:.5f}"},
        "ServiceCode": f"LCA{random.randint(10000, 99999)}",
    }})
(OUT / "travel_offers.json").write_text(json.dumps({"root": {"Page": offers}}, ensure_ascii=False))


# ---------------------------------------------------------------- financials workbook (2 sheets, with quirks)
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "Financials1"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
ws1.append(["Account", "Businees Unit", "Currency", "Year", "Scenario", *MONTHS])   # typo kept on purpose
ACCOUNTS = [("Sales", 1), ("Cost of Goods Sold", -0.45), ("Commissions Expense", -0.05), ("Payroll Expense", -0.12),
            ("Travel & Entertainment Expense", -0.02), ("R&D Expense", -0.08), ("Rent Expense", -0.03),
            ("Marketing Expense", -0.04), ("Other Expense", -0.01)]
for unit, scale in (("Software", 80e6), ("Advertising", 30e6), ("Hardware", 50e6)):
    for year in range(2012, 2016):
        scenarios = ["Actuals"] if year < 2015 else ["Actuals", "Budget", "Forecast"]
        for scenario in scenarios:
            for account, factor in ACCOUNTS:
                ws1.append([account, unit, "USD", year, scenario,
                            *[int(scale * factor * random.uniform(0.6, 1.2)) for _ in MONTHS]])

ws2 = wb.create_sheet("Financials2")
ws2.append(["Segment", "Country", "Product", "Discount Band", "Units Sold", "Manufacturing Price", "Sale Price",
            "Gross Sales", "Discounts", " Sales", "COGS", "Profit", "Date", "Month Number", "Month Name", "Year"])  # " Sales" kept
SEGMENTS = [("Government", 3), ("Midmarket", 1), ("Channel Partners", 1), ("Enterprise", 1), ("Small Business", 1)]
PRODUCTS = [("Atlas", 3), ("Borealis", 5), ("Cirrus", 10), ("Delta", 120), ("Equinox", 250), ("Fjord", 260)]
for _ in range(700):
    segment = random.choices([s[0] for s in SEGMENTS], weights=[s[1] for s in SEGMENTS])[0]
    product, mprice = random.choice(PRODUCTS)
    sale_price = random.choice([7, 12, 15, 20, 125, 300, 350])
    units = round(random.uniform(200, 4500) * 2) / 2
    band, disc = random.choices([("None", 0), ("Low", 0.02), ("Medium", 0.07), ("High", 0.12)], weights=[1, 3, 5, 5])[0]
    gross = int(units * sale_price)
    discounts = int(gross * disc)
    sales = gross - discounts
    cogs = int(units * mprice * 2.5) if mprice > 50 else int(units * mprice * 5)
    date = dt.datetime(random.choice([2013, 2014, 2014, 2014]), random.randint(1, 12), 1)
    ws2.append([segment, random.choice(["Canada", "Germany", "France", "Mexico", "United States of America"]), product, band,
                units, mprice, sale_price, gross, discounts, sales, cogs, sales - cogs, date, date.month,
                date.strftime("%B"), str(date.year)])   # year stored as text on purpose
wb.save(OUT / "financials_sample.xlsx")


# ---------------------------------------------------------------- HR employees (15 000 rows, original column names)
with open(OUT / "hr_employees.csv", "w") as f:
    f.write("satisfaction_level,last_evaluation,number_project,average_montly_hours,time_spend_company,"
            "Work_accident,left,promotion_last_5years,Departments,salary\n")    # "montly" typo kept
    departments = ["sales", "technical", "support", "IT", "product_mng", "marketing", "RandD", "accounting", "hr", "management"]
    for _ in range(15000):
        satisfaction = round(random.uniform(0.09, 1.0), 2)
        projects = random.randint(2, 7)
        hours = int(random.gauss(200, 50))
        left = int(satisfaction < 0.45 and random.random() < 0.6 or random.random() < 0.08)
        f.write(f"{satisfaction},{round(random.uniform(0.36, 1.0), 2)},{projects},{max(96, min(310, hours))},"
                f"{float(random.randint(2, 10))},{int(random.random() < 0.14)},{left},{int(random.random() < 0.02)},"
                f"{random.choice(departments)},{random.choices(['low', 'medium', 'high'], weights=[49, 43, 8])[0]}\n")


# ---------------------------------------------------------------- personality (2 900 rows, ~2 % missing values)
def maybe(value, rate=0.02):
    return "" if random.random() < rate else value


with open(OUT / "personality.csv", "w") as f:
    f.write("Time_spent_Alone,Stage_fear,Social_event_attendance,Going_outside,Drained_after_socializing,"
            "Friends_circle_size,Post_frequency,Personality\n")
    for _ in range(2900):
        introvert = random.random() < 0.48
        r = (lambda lo, hi: float(random.randint(lo, hi)))
        row = [r(5, 11) if introvert else r(0, 4), "Yes" if introvert else "No",
               r(0, 3) if introvert else r(4, 10), r(0, 2) if introvert else r(3, 7),
               "Yes" if introvert else "No", r(0, 5) if introvert else r(6, 15),
               r(0, 3) if introvert else r(3, 10), "Introvert" if introvert else "Extrovert"]
        f.write(",".join(str(maybe(v)) if i < 7 else str(v) for i, v in enumerate(row)) + "\n")

for p in sorted(OUT.iterdir()):
    print(f"{p.name:<26} {p.stat().st_size / 1e6:6.2f} MB")
