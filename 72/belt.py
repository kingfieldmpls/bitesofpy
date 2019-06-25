from collections import OrderedDict
from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    if user_score < MIN_SCORE:
        return None

    list_of_belts = list(takewhile(lambda x: x <= user_score, HONORS))

    return HONORS.get(list_of_belts[-1])
