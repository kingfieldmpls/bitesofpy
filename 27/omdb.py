# Working with APIs is very common these days and lucky for us they increasingly return JSON (over XML). We saved OMDb responses for some cool movies that the template code loads in.

# Parse this data answering some questions:

# get_movie_data should return a list of movie dicts, so for each movie you convert the json file to a dict.
# now you have the data structure, loop through the movies and return the movie:
# with Comedy in Genres (get_single_comedy)
# that had the most nominations (get_movie_most_nominations)
# having the longest runtime (get_movie_longest_runtime)
# Expect to do some string parsing and type conversions here. We hope you like it, enjoy!


import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = "http://projects.bobbelderbos.com/pcc/omdb/"
MOVIES = ("bladerunner2049 fightclub glengary " "horrible-bosses terminator").split()
TMP = "/tmp"

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f"{movie}.json"
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, "*json"))


def get_movie_data(files=files):
    movie_data_dicts = []

    for file in files:
        with open(file, "r") as movie_data:
            movie_data_dicts.append(json.loads(movie_data.read()))

    return movie_data_dicts


def get_single_comedy(movies):
    for movie in movies:
        if "Comedy" in [
            single_genre.replace(",", "") for single_genre in movie["Genre"].split()
        ]:
            return movie["Title"]


def get_movie_most_nominations(movies):
    return max(movies, key=lambda x: int(x["Awards"].split()[-2]))["Title"]


def get_movie_longest_runtime(movies):
    return max(movies, key=lambda x: int(x["Runtime"].split()[0]))["Title"]
