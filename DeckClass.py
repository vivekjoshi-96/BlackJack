import itertools
import random


class Deck:
    def __init__(self, n):
        self.shoe = self.build_decks(n)

    @staticmethod
    def build_decks(n):
        decks = []
        for i in range(n):
            deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
            decks = decks + deck
        random.shuffle(decks)
        return decks
