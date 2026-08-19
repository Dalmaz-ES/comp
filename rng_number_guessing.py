
#RANDOM USE
"""
import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


#number = random.randint(low, high) # returns a random integer between low and high
#number = random.random() # returns a random number between 0 and 1
#number = random.choice(options) # returns a random element from the options tuple

random.shuffle(cards) # shuffles the cards
print(cards)
"""


#NUMBER GUESSING GAME

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

is_running = True

print("Welcome to number guessing game, I'm thinking of a number")
print(f"Take a guess between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is not between the range")
            print(f"Take a guess between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low try again")
        elif guess > answer:
            print("Too high try again")
        elif guess == answer:
            print(f"You got it! It took you {guesses} guesses")
            is_running = False

    else:
        print("Please enter a valid number")
        print(f"Take a guess between {lowest_num} and {highest_num}")