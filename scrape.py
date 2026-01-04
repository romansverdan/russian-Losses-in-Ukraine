import requests
import csv
import os
import re
from bs4 import BeautifulSoup
from datetime import date, datetime
import sys
import json

URL = "https://index.minfin.com.ua/en/russian-invading/casualties/2025-11/"
CSV_FILE = "data/russia_losses.csv"
WAR_START = date(2022, 2, 24)

def extract_number(text):
    text = re.sub(r"\(.*?\)", "", text)
    text = text.replace("aprx.", "")
    digits = re.findall(r"\d+", text.replace(" ", ""))
    return int("".join(digits)) if digits else ""


response = requests.get(URL, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

today = soup.select_one("li.gold")
if not today:
    raise RuntimeError("Today's data block not found")

#date
raw_date = today.select_one("span.black").text.strip()
d, m, y = raw_date.split(".")
iso_date = f"{y}-{m}-{d}"

parsed_date = date(int(y), int(m), int(d))
day_number = (parsed_date - WAR_START).days + 2

#defaults
row = {
    "date": iso_date,
    "day": day_number,
    "personnel": "",
    "tanks": "",
    "apv": "",
    "artillery": "",
    "mlrs": "",
    "aaws": "",
    "aircrafts": "",
    "helicopters": "",
    "uav": "",
    "cruise_missiles": "",
    "warships": "",
    "vehicles_fuel_tanks": "",
    "special_equipment": "",
    "submarines": "",
}

for li in today.select("div.casualties ul li"):
    label = li.text.lower()
    value = extract_number(li.text)

    if "military personnel" in label:
        row["personnel"] = value
    elif "tanks" in label:
        row["tanks"] = value
    elif "armored fighting vehicle" in label:
        row["apv"] = value
    elif "artillery systems" in label:
        row["artillery"] = value
    elif "mlrs" in label:
        row["mlrs"] = value
    elif "anti-aircraft" in label:
        row["aaws"] = value
    elif "planes" in label:
        row["aircrafts"] = value
    elif "helicopters" in label:
        row["helicopters"] = value
    elif "uav" in label:
        row["uav"] = value
    elif "cruise" in label:
        row["cruise_missiles"] = value
    elif "ships" in label:
        row["warships"] = value
    elif "cars and cisterns" in label:
        row["vehicles_fuel_tanks"] = value
    elif "special equipment" in label:
        row["special_equipment"] = value
    elif "submarines" in label:
        row["submarines"] = value

#prevent duplicates
existing_dates = set()
if os.path.exists(CSV_FILE):
    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            existing_dates.add(r["date"])

if iso_date in existing_dates:
    print("Already recorded:", iso_date)
    sys.exit(0)

#append
with open(CSV_FILE, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=row.keys())
    writer.writerow(row)

print("Added:", iso_date)
