import csv
import re
import time

import requests
from bs4 import BeautifulSoup


def get_country_info(country_name):
    url = f"https://en.wikipedia.org/wiki/{country_name.replace(' ', '_')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    infobox = soup.find("table", class_="infobox")

    if not infobox:
        print(f"Infobox for {country_name} doesn't exist")
        return None

    country_data = {
        "country": country_name,
        "city": "Unknown",
        "area": "Unknown",
        "population": "Unknown",
    }

    for row in infobox.find_all("tr"):
        header = row.find("th")
        value = row.find("td")

        if not header or not value:
            continue

        header_text = header.get_text(strip=True).lower()
        value_text = value.get_text(strip=True)

        if any(word in header_text for word in ["capital", "largest city", "seat"]):
            city_clean = re.sub(
                r"\s*\d+°\d+[′″]?[NSWE]?.*", "", value_text.split("[")[0]
            ).strip()
            country_data["city"] = city_clean

        elif any(
            word in header_text
            for word in ["area", "land area", "surface area", "total area"]
        ):
            value_clean = value_text.replace("\xa0", " ").strip()
            area_match = re.search(
                r"([\d,.]+)\s*?(km²|square km|sq km|sq. km|sq mi|square miles|sq. mi)",
                value_clean,
            )

            if area_match:
                country_data["area"] = re.sub(r",", "", area_match.group(1)).strip()

        elif (
            ("population" in header_text)
            or ("estimate" in header_text)
            or ("census" in header_text)
        ):
            pop_values = re.findall(r"\d[\d,]*", value_text)
            if pop_values:
                pop_ints = [int(p.replace(",", "")) for p in pop_values]
                country_data["population"] = str(max(pop_ints))
    print(f"FINAL DATA for {country_name}: {country_data}")
    return country_data


with open("Countries.txt", "r", encoding="utf-8") as file:
    countries = [line.strip() for line in file]

with open("cities_data.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(
        csvfile, fieldnames=["country", "city", "area", "population"]
    )
    writer.writeheader()
    for country in countries:
        data = get_country_info(country)
        if data:
            writer.writerow(data)
            csvfile.flush()
        time.sleep(1)
