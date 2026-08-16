cart = []
total = 0

while True:
    food = input("Enter a food (q to exit): ")
    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of {food}: $"))
        quantity = int(input(f"Enter the quantity of {food}: "))
        
        cart.append({
            "food": food,
            "price": price,
            "quantity": quantity
        })

print("\n----- YOUR RECEIPT -----")

total = 0
for item in cart:
    subtotal = item["price"] * item["quantity"]
    total += subtotal
    print(f"{item['food']} x{item['quantity']} = ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f}")


