import random
print(" WELOME TO THE DICE ROLL  GAME")

choice = input("Do You Want to start the game (y/n) : ")
while choice :
    True
    choice = input("Do You Want to start the game (y/n) : ")
    if choice == "y ":
        game()
    if choice == "n" :
        break

def game():
    player_choice = int(input("Roll the dice (1 to 6 ) : "))
    ch=[1,2,3,4,5,6]
    computer_choice = random.choices(ch)

    return (player_choice,computer_choice)
result = game()
print(result)
