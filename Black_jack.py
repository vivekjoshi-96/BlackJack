import random
class player:
    def __init__(self, name=""):
        self.name = name
        self.playerhand=[]
        self.total = 0
        self.deal()
        self.bust=False

    def deal(self):
            self.playerhand.append(random.randint(1,10))
            self.playerhand.append(random.randint(1, 10))
            print("Player has "+str(self.playerhand[0])+" and "+ str(self.playerhand[1]))

    def hit(self):
        cardvalue = random.randint(1,10)
        playerhand.append(cardvalue)
        self.add()

    def show(self):
        print(self.name+ ",Your cards are" + str(self.playerhand)+ " and points are:" +str(self.total))

    def add(self):

       for x in self.playerhand:
        self.total=self.total+x

class dealerclass:
    def __init__(self):
        self.name='dealer'
        self.bust=False
        self.final=False
        self.dealerhand=[]

    def hit(self):
        cardValue = random.randint(1,10)
        dealerhand.append(cardValue)

    def deal(self):
        while len(dealerhand) != 2:
            dealerhand.append(random.randint(1,10))

    def show(self):
        print("Dealer has \"X \" &", +str(dealerhand[0] ))

    def add(self):
        for x in self.playerhand:
            self.total = total + x


class Card:
    def __init__(self, value):
        self.value = value
        colors = ['heart', 'diamonds', 'spades', 'clubs']
        deck = [Card(value) for value in range(1, 14) for color in colors]


def main():
    Nop = int(input("Enter the number of players"))
    if (Nop >= 1):
        player_objects = []
        for i in range(Nop):
            playername=input("enter your name")
            player_objects.append(player(playername))
        dealer = dealerclass()

    eleminated_count=0
    while (eleminated_count<len(player_objects)):
        for active in player_objects:
            if active.bust==False:
                print(active.name + "'s turn")
                active.add()
                active.show()
                if active.total <= 21:
                    action = input("Hit or stay?(h/s)")
                    if action == "h":
                        active.hit()
                        active.add()
                        if active.total > 21:
                            active.bust = True
                            eleminated_count = eleminated_count + 1
                        active.show()
                        print("Your points are", active.total)
                        break
                    elif action == 's':
                        break
                    else:
                        print("invalid input")

    while dealer.bust==dealer.final:
        if dealer.total < 17:
            dealer.hit()
            dealer.add()
            dealer.show()
            print("The dealer's points are: " + str(dealer.total))
        elif dealer.total > 21:
            dealer.player_bust = True
            print("Dealer Busted")
        else:
            dealer.final=True


if __name__ == '__main__':
    main()