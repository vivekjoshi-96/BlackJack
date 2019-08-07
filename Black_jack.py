from PythonTrack import PlayerClass
from PythonTrack import DealerClass
from PythonTrack import DeckClass


def gameplay():
    nop = int(input("Enter the number of players"))
    if nop >= 1:
        nod = int(input("Enter the number of decks"))
        shoe = []
        cards = DeckClass.Deck(nod)
        deck = cards.shoe
        shoe = shoe + deck
        card1 = shoe.pop(-1)
        card2 = shoe.pop(-1)
        dealer = DealerClass.Dealer(card1, card2)
        player_objects = []
        for i in range(nop):
            card1 = shoe.pop(-1)
            card2 = shoe.pop(-1)
            player_name = input("enter name for player" + ' ' + str(i+1) + ':')
            player_objects.append(PlayerClass.Player(player_name, card1, card2))
        eliminated_players = 0
        while eliminated_players < len(player_objects):
            for active_player in player_objects:
                while active_player.bust is False and active_player.final is False:
                    print(active_player.name + '\'s  turn', end='\n')
                    active_player.show()
                    dealer.show_single_card()
                    choice = int(input("enter 1 to hit or 2 to stay"))
                    if choice == 1:
                        card = shoe.pop(-1)
                        active_player.hit(card)
                        active_player.show()
                        if active_player.bust is True:
                            eliminated_players = eliminated_players + 1
                    if choice == 2:
                        active_player.stay()
                        eliminated_players = eliminated_players + 1
        dealer.show()
        dealer.add()
        while True:
            if dealer.black_jack is True:
                print("Dealer wins")
                exit()
            for player in player_objects:
                if player.bust is False:
                    if player.black_jack is True:
                        print(player.name + ' won', end='\n')
                    elif player.total == dealer.total:
                        print("Hand tied", end='\n')
                    elif player.total > dealer.total or dealer.bust is True:
                        print(player.name + 'won', end='\n')
                    else:
                        print("Dealer won")
    else:
        print("invalid input")


if __name__ == '__main__':
    gameplay()
