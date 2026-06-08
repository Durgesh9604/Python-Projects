import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    options = ["rock", "paper", "scissors"]

    if player_choice not in options:
        print("Invalid choice!")
        return None

    computer_choice = random.choice(options)

    return {
        "player": player_choice,
        "computer": computer_choice
    }


def check_win(player, computer):
    print("User chose =", player)
    print("Computer chose =", computer)

    if player == computer:
        return "It is a TIE!"

    elif player == "rock" and computer == "scissors":
        return "Rock breaks Scissors! You Win!"

    elif player == "rock" and computer == "paper":
        return "Paper covers Rock! Computer Wins!"

    elif player == "scissors" and computer == "rock":
        return "Rock breaks Scissors! Computer Wins!"

    elif player == "scissors" and computer == "paper":
        return "Scissors cut Paper! You Win!"

    elif player == "paper" and computer == "scissors":
        return "Scissors cut Paper! Computer Wins!"

    else:
        return "Paper covers Rock! You Win!"


while True:
    print("""
1. Start
2. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        choices = get_choices()

        if choices:
            result = check_win(
                choices["player"],
                choices["computer"]
            )
            print(result)

    elif choice == "2":
        print("Exiting the Playground!")
        break

    else:
        print("Invalid choice!")
