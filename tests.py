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