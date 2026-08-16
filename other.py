"""""

sinay = True
simay = True

if sinay:
    print("Sinay is avaiable")
else :
    print("Sinay is not avaiable")

"""""

"""""
age = int(input("Enter your age: "))
#or age = int(age)
age = age + 1

print(f"You are {age} years old !")

"""""

"""""
#AREA LENGTH

length = float(input("Enter your length: "))
length_2 = float(input("Enter your other length: "))

area = length * length_2
print(f"Your area is {area} square meters")
# numlock + alt + 0178 = KARESİ
"""""

"""""

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2) # pow(radius, 2) is the same as radius ** 2

print(f"The area of the circle is: {round(area, 3)}cm^2") # round the result to 3 decimal places

"""""

"""""
bananaprice = 7.49
appleprice = 5.95
item = input("Enter an item: ")
quantity = int(input("Enter a quantity: "))
total = quantity * appleprice


if item == "apple":

    print(f"The total is {total}")

elif item == "banana":
    print(f"The total is {bananaprice * quantity}")

else:
    print("Not a valid item")
"""""

"""""
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
"""""

#AT 1:00:12


"""""
phonenumber = input("Enter your phone number: ")

number = phonenumber.count(" ")
print(f"Your number has {number} dashes")
"""""

"""""
phonenumber = input("Enter your phone number: ")

number = phonenumber.replace(" ", "-")
print(f"Your is {number} ")
"""""

#print(help(str))
"""""
username = input("Enter your username: ")

if len(username) > 12:
    print("Your username is too long try again")

elif " " in username:
    print("Your username cannot have spaces")

elif not username.isalpha():
    print("Your username cannot have digits")

else:
    print(f"Your user name '{username}' is valid ")
"""""


"""""
c_num = input("Enter your credit card number:  ")

if len(c_num) > 19:
    print("Invalid credit card number")

if " " in c_num:
    c_num = c_num.replace(" ", "-")
    print(c_num)

#has_spaces = " " in c_num
#if has_spaces is True:
#    c_num = c_num.replace(" ", "-")
#    print(c_num)
"""""



#LOOK THIS UP TO THE ELLSE PART
"""""
c_num = input("Enter your credit card number: ")
c_num = c_num.replace(" ", "").replace("-", "")  # Remove spaces and dashes

if not c_num.isdigit() or len(c_num) != 16: # Check if all characters are digits and length is 16
    print("Invalid credit card number. It must be exactly 16 digits.")
else:
    formatted = '-'.join([c_num[i:i+4] for i in range(0, 16, 4)]) # Format as XXXX-XXXX-XXXX-XXXX
    print(formatted)
"""""


#CHECK AGAIN THE FORMAT SPECIFIERS

"""""
price1 = 3000.12356
price2 = -1075.99
price3 = 1000.456

#print(f"Price1 is ${price1:.3f}") # .2f = 2 decimal places
#print(f"Price2 is ${price2:07}") # 07 = 7 spaces
#print(f"Price3 is ${price3:10}") # 10 = 10 spaces
#print(f"Price3 is ${price3:>9}") # > = right align
#print(f"Price3 is ${price3:^10}") # ^ = center align
#print(f"Price3 is ${price3:+}") # + = add a + sign to positive numbers

#print(f"price 1 is ${price1: }") # space = add a space before positive numbers
#print(f"price 2 is ${price2: }")
#print(f"price 3 is ${price3: }")

print(f"price 1 is ${price1:+,.2f}") # , = comma separator for thousands
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")
"""""


"""""
num = int(input("Enter a number between 1 and 10 (or type 11 to quit): "))

while num != 11:
    if num < 1 or num > 10:
        print("Invalid number")
        num = int(input("Please enter a valid number between 1 and 10: "))
    else:
        print(f"The number {num} is valid")
        break

print("Bye for now")
"""""




#!!!! IMPORTANT !!!!!
"""""
num = input("Enter a number between 1 and 10 (or type q to quit): ")

while num != "q":
    if num.isdigit():
        num = int(num)
        if num < 1 or num > 10:
            print("Invalid number")
            num = input("Please enter a valid number between 1 and 10: ")
        else:
            print(f"The number {num} is valid")
            break
    else:
        print("Invalid input")
        num = input("Please enter a valid number between 1 and 10: ")

if num == "q":
    print("Game ended")
"""""

"""""
import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)): # counts up from 0 to my_time
    print(x)                          # OR for x in range(my_time, 0, -1):
    time.sleep(1) # waits for 1 second
print("Time's up")
"""""

"""""
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()
"""""

"""""
fruits = ["apple", "orange", "banana", "coconut"]

print("lime" in fruits)
"""""




foods = []
prices = []
total = 0

while True:
    food = input("Enter a food (q to exit): ")
    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food) # adds the food to the list
        prices.append(price) # adds the price to the list

print("-----YOUR CART----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")
