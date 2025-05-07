import requests
import csv
import time
from bs4 import BeautifulSoup
import re


def get_country_info(country):
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
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
        print(f"Information doesn't found for  {country}")
        return None

    data = {
        "country": country,
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

        if any(
            word in header_text for word in ["capital", "largest city", "seat"]
        ):
            city_clean = re.sub(
                r"\s*\d+°\d+[′″]?[NSWE]?.*", "", value_text.split("[")[0]
            ).strip()
            data["city"] = city_clean

        elif ("area" in header_text) or (
            ("total" in header_text)
            and ("km" in value_text or "sq" in value_text)
        ):
            area_match = re.search(
                r"([\d,]+)\s*km[²2]?", value_text, re.IGNORECASE
            )
            if area_match:
                data["area"] = area_match.group(1).replace(",", "")

        elif (
            ("population" in header_text)
            or ("estimate" in header_text)
            or ("census" in header_text)
        ):
            pop_values = re.findall(r"\d[\d,]*", value_text)
            if pop_values:
                pop_ints = [int(p.replace(",", "")) for p in pop_values]
                new_pop = max(pop_ints)
                if (
                    data["population"] == "Unknown"
                    or int(data["population"]) < new_pop
                ):
                    data["population"] = str(new_pop)

    print(f"Data for {country}: {data}")

    return data


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
