import random
choice = input("Do you want to start the game?(y/n)").lower()
if choice == "y" :

    player_choice = int(input("Enter the number from Dice (1 to 6) : "))
    print("\n")
    if player_choice > 6 :
        print("Invalid choice !")
    else:
            options = [1,2,3,4,5,6]
            computer_choice = random.choice(options)

            print(f"Player Choice is {player_choice}")
            
            print(f"Computer Choice is {computer_choice}")
            result = [player_choice , computer_choice]
            print(result)
            if player_choice == computer_choice:
                print("Match is tied")

            elif player_choice > computer_choice:
                print("Hurray ! Player won the match.")

            else:
                print(" Computer won the match !")

else :
    print("Exiting the game....")
