#FILM STAND PROGRAM EASY
"""
menu = {"popcorn": 10.50,
        "chips": 12.00,
        "drinks": 8.25,
        "water": 1.50}

cart = []
total = 0

print("----- POPCORN STAND MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    choice = input("Enter your choice (q to quit): ").lower()
    if choice == "q":
        break

    elif choice in menu:
        cart.append(choice)
        total += menu[choice]
    else:
        print("Invalid choice")

print("----- YOUR CART -----")
for food in cart:
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")
"""



#FILM STAND PROGRAM HARD
"""
menu = {"popcorn": 10.50,
         "chips": 12.00,
         "drinks": 8.25,
         "water": 1.50}

cart = []
total = 0

print("----- POPCORN STAND MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    choice = input("Enter your choice (q to quit): ").lower()
    if choice == "q":
        break

    elif choice in menu:
        while True:
            try:
                quantity = int(input(f"How many {choice} would you like? "))
                if quantity <= 0:
                    print("Invalid quantity")
                else:
                    for _ in range(quantity):
                        cart.append(choice)
                        total += menu[choice]
                    break
            except ValueError:
                print("Invalid quantity")
    else:
        print("Invalid choice")

print("----- YOUR CART -----")
displayed = set()
for food in cart:
    if food not in displayed:
        print(f"{food} x {cart.count(food)}")
        displayed.add(food)

print()
print(f"Total: ${total:.2f}")
"""


