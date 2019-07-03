import itertools
import random


class Deck:
    deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
    random.shuffle(deck)
