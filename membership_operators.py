
#  Membership Operators = used to test whether a value or variable is found in a sequence
#                         (string, list, tuple, set or dict)
#                         1. in
#                         2. not in

"""
word = "apple"

letter = input("Enter a letter: ").lower()

while letter

    if letter in word:
        print(f"The {letter} is in the word")

    elif letter not in word:
        print(f"The {letter} is not in the word")
"""


#Same example better
"""
word = "apple"
guessed_letters = []

while True:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("You guessed the word!")
        break

    guess = input("Enter a letter or q to quit: ").lower()

    if guess == "q":
        print("Thanks for playing!")
        break

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"The letter {guess} is in the word.")
    else:
        print(f"The letter {guess} is not in the word.")
"""


#example on sets, list and tuples and sets ll behave similar
"""
students = {"john", "jane", "bob", "alice"}

student = input("Enter a name to search: ").lower()

if student in students:
    print(f"{student} is in the list")
else:
    print(f"{student} is not in the list")
"""


#same example on sets with while loop
"""
students = {"john", "jane", "bob", "alice"}

while True:
    student = input("Enter a name to search (or 'q' to quit): ").strip().lower()
    if student == "q":
        print("Goodbye.")
        break
    if not student:
        print("Please enter a name.")
        continue
    if student in students:
        print(f"{student} is in the list")
        break
    print(f"{student} is not in the list — try again.")
"""



#example on dictionaries
"""
grades = {"Sandy": "A",
          "John": "B",
          "Jane": "A",
          "Bob": "C"}

student = input("Enter a name to search: ").capitalize()

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not in the list")
"""


#multiple conditions

email = "esd@gmail.com"

if "@" in email and "." in email:
    print("This is a valid email")

else:
    print("This is not a valid email")

