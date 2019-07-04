from PythonTrack import DeckClass


class Dealer:
    def __init__(self):
        self.name = 'dealer'
        self.bust = False
        self.black_jack = False
        self.dealer_hand = []
        self.total = 0
        self.final = False
        self.deal()

    def hit(self):
        while self.total < 17:
            self.dealer_hand.append(DeckClass.Deck.deck.pop(-1))
            self.dealer_hand.sort(reverse=True)
            self.add()
        if self.total>21:
            self.bust=True
        if len(self.dealer_hand) == 2 and self.total == 21:
            self.black_jack = True

    def deal(self):
        self.dealer_hand.append(DeckClass.Deck.deck.pop(-1))
        self.dealer_hand.append(DeckClass.Deck.deck.pop(-1))
        self.dealer_hand.sort(reverse=True)
        self.add()
        self.hit()

    def add(self):
        self.total = 0
        for i in range(len(self.dealer_hand)):
            value = self.dealer_hand[i][0]
            if value > 10:
                value = 10
            if value == 1 and self.total <= 10:
                value = 11
            self.total += value

    def show(self):
        print("dealer's cards are")
        for i in range(len(self.dealer_hand)):
            print(self.dealer_hand[i][0], "of", self.dealer_hand[i][1], end='\n')

        print("and points are:" + str(self.total))
