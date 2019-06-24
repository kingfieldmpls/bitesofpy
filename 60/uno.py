from collections import namedtuple
import pdb

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    standard_cards = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "Skip",
        "Reverse",
        "Draw Two",
    ]

    uno_deck = []

    for suit in SUITS:
        uno_deck.append(UnoCard(suit, "0"))
        uno_deck.append(UnoCard(None, "Wild"))
        uno_deck.append(UnoCard(None, "Wild Draw Four"))

    for suit in SUITS * 2:
        for card in standard_cards:
            uno_deck.append(UnoCard(suit, card))
    return uno_deck
