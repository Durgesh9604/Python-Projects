
import random

def get_choices():
    player_choice =input("Enter the user choice (rock,paper,scissors) :")
    options = ["rock","paper","scissors"]
    
    computer_choice = random.choice(options)

    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print("User choose = "+player)
    print("Computer choose = "+computer)
    
    if (player == computer):
        return "It is a TIE !"
    
    elif player =="rock" and computer == "scissors":
        return "Rock brokes the scissors ! You Win !"
    
    elif player == "rock" and computer == "paper":
        return "Paper Grabs Rock ! Computer Win !"
    
    elif player == "scissors" and computer == "rock":
        return "Rock brokes the scissors ! Computer Win !"

    elif player == "scissors" and computer == "paper":
        return "Scissor cuts the Paper ! You Win !"
    elif player == "paper" and computer == "scissors":
        return "Scissor cuts the Paper ! Computer Win !"

    else :
        return "Paper Grabs Rock ! You Win !"

choices = get_choices()

result = check_win(choices["player"],choices["computer"])
print(result)
