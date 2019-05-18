# In this Bite you are provided with a list of publish dates of all our PyBites blog posts. They are in this format: Thu, 04 May 2017 20:46:00 +0200.

# Write a function called convert_to_datetime that takes a date string and convert it to a datetime object. You can leave the timezone part (e.g. +0200) off.

# Secondly complete the get_month_most_posts function: it should take a list of datetime objects and return the month that we posted the most. You should get 2017-01. See also the TESTS tab how your code will be tested.

# Have fun and let us know how you experienced this Bite. Have fun!


import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = "http://projects.bobbelderbos.com/pcc/dates/"
RSS_FEED = "all.rss.xml"
PUB_DATE = re.compile(r"<pubDate>(.*?)</pubDate>")
TMP = "/tmp"


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


dates = _get_dates()


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    return datetime.strptime(date_str[:-6], "%a, %d %b %Y %H:%M:%S")


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    date_format = "%Y-%m"
    month_list = [date.strftime(date_format) for date in dates]
    return collections.Counter(month_list).most_common(1)[0][0]
