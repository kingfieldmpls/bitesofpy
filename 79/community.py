import csv

from collections import Counter

import requests

CSV_URL = "https://bit.ly/2HiD2i8"


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    csv_response = requests.get(CSV_URL).content.decode("utf-8")

    reader = csv.DictReader(csv_response.splitlines())

    return reader


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    tz = [item["tz"] for item in content]

    c = Counter(tz)

    for k, v in sorted(c.items()):
        bar = "+" * v
        print(f"{k:<21}| {bar}")
