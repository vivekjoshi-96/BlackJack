class Player:
    def __init__(self,  name, card1, card2):
        self.name = name
        self.player_hand = []
        self.total = 0
        self.deal(card1, card2)
        self.bust = False
        self.black_jack = False
        self.final = False

    def deal(self, card1, card2):
        self.player_hand.append(card1)
        self.player_hand.append(card2)
        self.player_hand.sort(reverse=True)

    def show(self):
        print("your cards are")
        for i in range(len(self.player_hand)):
            print(self.player_hand[i][0], "of", self.player_hand[i][1], end='\n')
        self.add()
        print("and points are:" + str(self.total))

    def add(self):
        self.total = 0
        for i in range(len(self.player_hand)):
            value = self.player_hand[i][0]
            if value > 10:
                value = 10
            if value == 1 and self.total <= 10:
                value = 11
            self.total += value
        if self.total > 21:
            self.bust = True
        if self.total == 21 and len(self.player_hand) == 2:
            self.black_jack = True

    def hit(self, card):
        self.player_hand.append(card)
        self.player_hand.sort(reverse=True)

    def stay(self):
        self.final = True
