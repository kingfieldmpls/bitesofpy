# In this bite a real world scenario: PyBites has a growing set of Bites and gives away promos. They choose a Bite randomly but don't want to choose the same one again.

# Hence you are provided with a BITES constant (subset to keep it on the screen) and a bites_done set that gets passed into the class via its constructor. Complete the methods in the Promo class:

# _pick_random_bite is a helper (_ here means private) that picks a randomly available Bite. When no more Bites are available raise a NoBitesAvailable (provided).
# new_bite should use this helper and update self.bites_done (it keeps state, the reason we used a class here).
# See also the tests. We hope you learn a thing or two. Enjoy!

import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    def _pick_random_bite(self):
        if len(BITES) == len(self.bites_done):
            raise NoBitesAvailable()

        bites_set = set(BITES.keys())
        available_bites = bites_set - self.bites_done
        return random.sample(available_bites, 1)[0]

    def new_bite(self):
        next_bite = self._pick_random_bite()
        self.bites_done.add(next_bite)
        return next_bite
