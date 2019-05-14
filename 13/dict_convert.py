# Write a function to convert the given blog dict to a namedtuple.

# Write a second function to convert the resulting namedtuple to json.

# Here you probably need to use 2 of the _ methods of namedtuple :)

from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

bloggy = namedtuple('bloggy', ['name', 'founders', 'started', 'tags', 'location', 'site'])

def dict2nt(dict_):
    return bloggy._make(dict_.values())


def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)
