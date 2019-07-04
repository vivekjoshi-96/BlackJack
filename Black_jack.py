from PythonTrack import PlayerClass
from PythonTrack import DealerClass


def gameplay():
    game_tied = False
    leader_score = 0
    nop = int(input("Enter the number of players"))
    if nop >= 1:
        player_objects = []
        for i in range(nop):
            player_name = input("enter name for player" + ' ' + str(i+1) + ':')
            player_objects.append(PlayerClass.Player(player_name))
        eliminated_players = 0
        while eliminated_players < len(player_objects):
            for active_player in player_objects:
                if active_player.bust is False and active_player.final is False:
                    print(active_player.name + '\'s  turn')
                    active_player.show()
                    choice = int(input("enter 1 to hit or 2 to stay"))
                    if choice == 1:
                        active_player.hit()
                        if active_player.bust is True:
                            eliminated_players = eliminated_players+1
                    if choice == 2:
                        active_player.stay()
                        eliminated_players = eliminated_players+1
        dealer_object = []
        dealer_object.append(DealerClass.Dealer())
        for dealer in dealer_object:
            dealer.show()
            leader_score = dealer.total
        while True:
            leader = ''
            for dealer in dealer_object:
                if dealer.black_jack is True:
                    print("Dealer wins")
            for player in player_objects:
                for dealer in dealer_object:
                    if player.bust is False:
                        if player.black_jack is True:
                            print(player.name + 'won', end='\n')
                        if player.total == leader_score:
                            game_tied = True
                        if player.total > leader_score or dealer.bust is True:
                            print(player.name + ' is in the lead', end='\n')
                            leader_score = player.total
                            game_tied = False
                            leader = player.name
            if leader == '':
                print("Dealer won")
            else:
                if game_tied is False:
                    print(leader + ' won', end='\n')
                if game_tied is True:
                    print('There was a tie', end='\n')
                break
            break
    else:
        print("invalid input")


if __name__ == '__main__':
    gameplay()
