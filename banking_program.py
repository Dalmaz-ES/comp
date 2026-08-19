
#BANKING PROGRAM

def show_balance(balance):
    print("----------------------")
    print(f"Your current balance is ${balance:.2f}")
    print("----------------------")

def deposit():
    print("----------------------")
    amount = float(input("Enter the amount to deposit: "))
    print("----------------------")

    if amount <= 0:
        print("Please enter a positive amount")
        return 0
    else:
        return amount


def withdraw(balance):
    print("----------------------")
    amount = float(input("Enter the amount to withdraw: "))
    print("----------------------")

    if amount <= 0:
        print("Please enter a positive amount")
        return 0
    elif amount > balance:
        print("Not sufficient funds")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------------")
        print("Banking program")
        print("----------------------")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("----------------------")
        print(f"Current balance: ${balance:.2f}")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid choice")

    print("Thank you for using this program")

if __name__ == '__main__':
    main()
    