# Russian Losses in Ukraine

Daily updated data of Russian losses in Ukraine since **February 24, 2022**.  
Data is collected from the official Ukrainian General Staff reports (**@GeneralStaffUA**) and scraped automatically from [index.minfin.com.ua](https://index.minfin.com.ua/en/russian-invading/casualties/).

---

## 📄 Data Files

- **CSV:** `data/russia_losses.csv` – daily cumulative losses  

---

## 🗂 CSV Columns

| Column | Description |
|--------|-------------|
| `date` | Date of the report (`YYYY-MM-DD`) |
| `day` | Number of days since February 24, 2022 |
| `personnel` | Military personnel losses |
| `tanks` | Tanks losses |
| `apv` | Armored personnel vehicles losses |
| `artillery` | Artillery systems losses |
| `mlrs` | Multiple launch rocket systems losses |
| `aaws` | Anti-aircraft warfare systems losses |
| `aircrafts` | Aircrafts losses |
| `helicopters` | Helicopters losses |
| `uav` | Operational-tactical UAV losses |
| `cruise_missiles` | Cruise missile losses |
| `warships` | Warships losses |
| `vehicles_fuel_tanks` | Vehicles and fuel tanks losses |
| `special_equipment` | Special equipment losses |
| `submarines` | Submarines losses |

---

## ⚙️ Automation

This repository uses **GitHub Actions** to automatically:

1. Scrape the latest data from [index.minfin.com.ua](https://index.minfin.com.ua/en/russian-invading/casualties/)  
2. Append new rows to the CSV if the date is not already present  
3. Commit and push updates to the repository  

**Schedule:** Daily at **11:00 UTC / 13:00 Kyiv winter time / 14:00 Kyiv summer time**.

---

## 📝 Usage

You can use this data for:

- Analysis and visualization in Python, R, Excel, etc.  
- Loading into databases (SQLite, DuckDB, PostgreSQL)  
- Sharing or embedding in dashboards  

## 📝 Notes

- All numbers are cumulative totals reported for each day.
- Some fields may be empty if the source did not provide data for that category.
- The workflow is designed to avoid duplicate entries for the same date.
- Data is sourced from official reports but may have minor discrepancies.

## 📎 References

[Armed Forces of Ukraine](https://www.zsu.gov.ua/)

[MinFin Casualties Index](https://index.minfin.com.ua/en/russian-invading/casualties/)