
import random

options = ("rock", "paper", "scissors") # tuple because we are not changing the options
running = True

while running:

    player = None # resets player
    computer = random.choice(options) # chooses a random option from the options tuple

    while player not in options:
        player = input("Enter rock, paper or scissors: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        running = False

print("Thanks for playing!")




"""
elif player == "rock": #OR IN THIS FORMAT-> elif player == "rock" and computer == "scissors":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")

elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")

elif player == "scissors":
    if computer == "rock":
        print("You lose!")
    else:
        print("You win!")
"""
