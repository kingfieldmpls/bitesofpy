from datetime import datetime

BITE_CREATED_DT = datetime.strptime("2018-02-26 23:24:04", "%Y-%m-%d %H:%M:%S")

PT2_DEATH = datetime(2020, 4, 12)

miller_factor = 61320


def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    return round((PT2_DEATH - BITE_CREATED_DT).total_seconds() / 60 / 60, 2)


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    return round(py2_earth_hours_left() * 60 / miller_factor, 2)
