import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc_aware = pytz.utc.localize(utc)

    works = []

    for time in timezones:
        if time not in TIMEZONES:
            raise ValueError
        elif utc_aware.astimezone(pytz.timezone(time)).hour not in MEETING_HOURS:
            works.append(False)
        else:
            works.append(True)

    return all(works)
