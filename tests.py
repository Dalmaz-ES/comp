
#MARKET EXAMPLE
"""
banana_price = 7.49
apple_price = 5.95

item = input("Enter an item: ")

if item == "apple":
    quantity = int(input("Enter a quantity: "))
    print("The total is", quantity * apple_price)

elif item == "banana":
    quantity = int(input("Enter a quantity: "))
    print("The total is", quantity * banana_price)

else:
    print("Not a valid item")
"""



#QUIZ GAME TEST
"""
questions = ("WHATS MY NAME?: ",
             "WHATS MY AGE?: ",
             "WHATS M Y HEIGHT?: ",
             "WHATS MY COUNTRY?: ")

options = (("A.John", "B.Sinay", "C.Doe", "D.Smith"),
           ("A.22", "B.23", "C.24", "D.25"),
           ("A.5.7", "B.5.8", "C.5.9", "D.6.0"),
           ("A.USA", "B.Canada", "C.UK", "D.Australia"))

answers = ("B", "B", "C", "A")

guesses = []

score = 0
question_num = 0


for x in questions:
    print("-------------------------")
    print(x)

    for y in options[question_num]:
        print(y)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess) # adds the guess to the guesses list
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")

    else:
        print("WRONG!")
        print(f"{answers[question_num]}. is the correct answer")
    question_num += 1

print("-------------------------")
print("RESULTS")
print("-------------------------")

print("answers: ", end="")
for x in answers:
    print(x, end=" ")
print()

print("guesses: ", end="")
for x in guesses:
    print(x, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

if score >= 50:
    print("You passed the quiz")
else:
    print("You failed the quiz")
"""
