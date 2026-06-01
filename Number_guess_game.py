# Number guessing game

import random

print("************************WELCOME TO GAME*************************")
print("""
🎮 NUMBER GUESSING GAME 🎮

Instructions:
1. The computer has selected a random number between 1 and 100.
2. Your task is to guess the correct number.
3. After each guess:
   - If your guess is too high, you'll see "Too High!"
   - If your guess is too low, you'll see "Too Low!"
4. Keep guessing until you find the correct number.
5. Enter only numbers between 1 and 100.

Good Luck! 🍀
""")

guess_number = random.randint(1,101)

while True :

    player_number = int(input("Enter The Number Between (1 to 100) = "))
    print("The player number is ",player_number)

    if player_number == guess_number:
        print("Congratulation You Guessed The Correct Number ")
        print(f"The Guessed Number is {guess_number}")
        break

    elif player_number > guess_number:
        print("Too High")

    else :
        print("Too Low")
        
