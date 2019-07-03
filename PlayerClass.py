from PythonTrack import DeckClass


class Player():
    def __init__(self):
        #self.name = name
        self.player_hand = []
        self.total = 0
        self.deal()
        self.bust = False

    def deal(self):
        self.player_hand.append(DeckClass.Deck.deck.pop(-1))
        self.player_hand.append(DeckClass.Deck.deck[-1])
        self.player_hand.sort(reverse = True)
        self.add()
        self.show()

    def show(self):
        print("your cards are")
        for i in range(len(self.player_hand)):
            print(self.player_hand[i][0], "of", self.player_hand[i][1], end='\n')
        print("and points are:" + str(self.total))

    def add(self):
        for i in range(len(self.player_hand)):
            value = self.player_hand[i][0]
            if value > 10:
                value = 10
            if value == 1 and self.total <= 10:
                value = 11
            self.total += value

    def hit(self):
        self.player_hand.append(DeckClass.Deck.deck.pop(-1))
        self.player_hand.sort(reverse=True)
        self.add()
        self.show()


