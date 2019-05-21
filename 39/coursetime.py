# In this Bite you read in a text file with course times (MM:SS) per video.

# You extract these and calculate the total course duration in HH:MM:SS.

# See the docstrings and tests for more details.

# Have fun and we hope you learn a thing or two.

# Trivia: in honor of our Code Challenges Pilot: this was the exercise we used to test the waters when we started out :)


from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join("/tmp", "course_timings")
urllib.request.urlretrieve("http://bit.ly/2Eb0iQF", COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    text_time_format = re.compile("\\((\\d+:\\d+)\\)")

    with open(COURSE_TIMES, "r") as c_times:
        c_times_lines = c_times.readlines()

    c_just_times = " ".join(
        [line.strip() for line in c_times_lines if line.strip() != ""]
    )
    find_times = re.findall(text_time_format, c_just_times)

    return find_times


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    base_datetime = datetime(1900, 1, 1, 0, 0, 0)
    datetime_format = "%H:%M:%S"

    for times in timestamps:
        mins, secs = times.split(":")
        base_datetime = base_datetime + timedelta(minutes=int(mins), seconds=int(secs))

    return base_datetime.strftime(datetime_format).lstrip("0")
