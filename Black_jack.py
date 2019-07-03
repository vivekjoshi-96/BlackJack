from PythonTrack import PlayerClass


def main():
    #code to choose no of players and deal cards to them
    nop = int(input("Enter the number of players"))
    if nop >= 1:
        player_objects = []
        for i in range(nop):
            player_name = input("enter name for player" + ' ' + str(i+1) + ':')
            player_objects.append(PlayerClass.Player(player_name))
        eleminated_players = 0
        while eleminated_players < len(player_objects):
            for active_player in player_objects:
                if active_player.bust is False and active_player.final is False:
                    print(active_player.name + '\'s  turn')
                    active_player.show()
                    choice = input("enter 1 to hit or 2 to stay")
                    if choice == 1:
                        active_player.hit()
                        if active_player.bust is True:
                            eleminated_players += 1
                    if choice == 2:
                        active_player.stay()
                        eleminated_players += 1

    else:
        print("invalid input")


if __name__ == '__main__':
    main()
