
#SLOT MACHINE PROGRAM

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

#    results = []
#    for x in range(3):
#        results.append(random.choice(symbols))
#    return results #list comprehension can also be used

    return [random.choice(symbols) for x in range(3)] # same as above

def print_row(row):
    print("-----------------")
    print("  |  ".join(row))
    print("-----------------")

def get_payout(row, bet):
#    if row[0] == row[1] == row[2]:
#        return bet * 3
#    elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
#        return bet
#    else:
#        return 0

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():

    balance = 100
    print("***************************")
    print("Welcome to the slot machine")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***************************")

    while balance > 0:
        print(f"Your balance is: ${balance:.2f}")

        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("-----------")
            print("Invalid bet")
            print("-----------")
            continue

        bet = float(bet)

        if bet > balance:
            print("------------------")
            print("Insufficient funds")
            print("------------------")
            continue

        if bet <= 0:
            print("------------------")
            print("Bet must be greater than 0")
            print("------------------")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning row...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            balance += payout
            print(f"You won ${payout:.2f}")
        else:
            print("You lost")

        balance += payout

        play_again = input("Do you want to spin again (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"Thanks for playing! your balance is: ${balance:.2f}")

if __name__ == '__main__':
    main()

#5.58.55
