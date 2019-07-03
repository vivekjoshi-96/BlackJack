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