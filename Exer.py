"""""
#VARIABLES

#STRINGS
first_name = "John"
print(f"Hello {first_name}") #f-string to insert variable inside string

#INTEGERS
age = 25
print(f"John is {age} years old") #f-string

#FLOAT
height = 1.75
print(f"John is {height} meters tall") #f-string

#BOOLEAN
is_adult = True
print(f"John is an adult: {is_adult}") #f-string

is_student = False 
print(f"Are you a student?: {is_student}") #f-string

is_alien = False 

if is_alien:
    print("You are an alien")
else:
    print("You are not an alien")

"""""
from dataclasses import replace
from selectors import SelectSelector

"""""
#TYPECASTING, process of converting a variable from one data type to another str(), int(), float(), bool() 

name = "Sinay" #str
age = 23 #int
gpa = 3.16 #float
is_student = True #bool

print(type(is_student)) # shows the type of the variable

age = float(age) # convert integer to float
print(age)

gpa = int(gpa) # convert float to integer
print(gpa)

age += 1 # increment the age by 1
print(age)

age = str(age)
age += 1
print(age) # this will throw an error because you can't increment a string

age = str(age) # convert integer to string so rather than adding 24+1 it adds to the end of 24 so its 241
age += "1"
print(age)
"""""

"""""
#INPUT FUNCTION, allows user to input data into the program
#input() function returns as a string so we need to convert it to the required data type using typ


name = input("What is your name?: ") #input function returns a 
print(f"Welcome {name}")


age = int(input("How old are you?: "))

#age = int(age) # same thing as int(input())
age = age + 1

print(f"You are {age} years old")
"""""
"""""
#EXERCISE RECTANGLE

Length = float(input("Enter the length of the rectangle: "))
Width = float(input("Enter the width of the rectangle: "))

Area = Length * Width
print(f"Area of the rectangle is: {Area}")
"""""
"""""
#EXERCISE SHOPPING CART

item = input("What item would tou like to buy?: ")
price = float(input("Whats the price of the item?: "))
quantity = float(input("How many of those items would you like to buy?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Total is {total}$")
"""""
"""""
#MADLIBS GAME, word game where you fill in the blanks with words to create a funny story


adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")

print(f"Today i went to a {adjective1} zoo")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and had {adjective3} fur")
"""""

"""""
#ARITMETHIC OPERATORS


apple = 10
#apple **= 3
#apple *= 2
#apple /= 5
#apple += 10
#apple -= 5 # apple = apple - 5 [same things]
 
remainder = apple % 3 # returns the remainder of the division of apple by 3
print(remainder)
"""""

"""""
x = 3.14
y = 5
z = 7

#result = round(x) # returns the integer value of x
#result = abs(y) # returns the absolute value of y
#result = pow(x, y) # returns the value of x to the power of y
#result = max(x, y, z) # returns the highest value among x, y, z
#result = min(x, y, z) # returns the lowest value among x, y, z

print(result)
"""""

"""""
import math

x = 9.9
#print(math.pi) # returns the value of pi
#print(math.e) # returns the value of e
#result = math.sqrt(x) # returns the square root of x
#result = math.ceil(x) # returns the smallest integer value that is greater than or equal to x
#result = math.floor(x) # returns the largest integer less than or equal to x
print(result) 
"""""

"""""
#MATH EXERCISE

import math

radius = float(input('Enter the radius of the circle: '))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is: {round(circumference, 2)}") # round the result to 2 decimal places
"""""

"""""
import math 

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2) # pow(radius, 2) is the same as radius ** 2

print(f"The area of the circle is: {round(area, 3)}cm^2") # round the result to 3 decimal places
"""""

"""""
import math 

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))

hypotenuse = math.sqrt(height ** 2 + base ** 2) # math.sqrt(pow(height, 2) + pow(base, 2)) is the same 

print(f"The hypotenuse of the triangle is: {round(hypotenuse, 3)}") # round the result to 3 decimal places
"""""

"""""
#IF STATEMENTS, Do some code only if some condition is True. Else do something else

age = int(input("Enter you age: "))


if age >= 100:
    print("You are too old for credit")
elif age >= 18:
    print("You are eligable for credit")
elif age < 0:
    print("Please enter a valid age")

else: 
    print("You are not eligable for credit")
"""""

"""""
response = input("Do you like to play tennis? (yes/no): ")

if response == "yes":
    print("Play some tennis")

else:
    print("No tennis for you")
"""""

"""""
name = input("Please enter your name: ")

if name == "":
    print("Howdy, stranger! Enter your name to get a proper greeting!")

else:
    print(f"Welcome, {name}")
"""""

"""""
#USE OF BLOOEANS WITH IF STATEMENTS

for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
"""""
"""""
#PYTHON CALCULATOR

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
   result = num1 + num2
   print(round(result, 2)) #round to 2 decimal places
elif operator == "-":
   result = num1 - num2
   print(result)
elif operator == "*":
   result = num1 * num2
   print(result)
elif operator == "/":
   result = num1 / num2
   print(result)
else:
   print(f"You fool invalid '{operator}' operator") #f-string to insert operator into the string
"""""
"""""
#WEIGHT CONVERTER

weight = float(input("Enter your weight please: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.20462
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "L" or unit == "l":
    weight = weight / 2.20462
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"The {unit} is not valid")
"""""
"""""
#TEMPERATURE CONVERTER PROGRAM

temperature = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit? (C or F): ")

if unit == "C" or unit == "c":
    temperature = (temperature * 9/5) + 32
    unit = "F"
    print(f"The temperature is {round(temperature, 1)} {unit}")

elif unit == "F" or unit == "f":
    temperature = (temperature - 32) * 5/9
    unit = "C"
    print(f"The temperature is {round(temperature, 1)} {unit}") # round to 1 decimal place and adds the unit to the end of the string 

else: 
    print(f"The unit {unit} is not valid")
"""""

#LOGICAL OPERATORS, evaluate multipe conditions (or, and, not)
#                   or = at least one condition must be true 
#                   and = both conditions must be true
#                   not = inverts the condition (not False, not True)

"""

temp = float(input("Enter the temperature: ") )
is_raining = True


if temp >= 25 and not is_raining:
    print("It's a beautiful day") 
elif temp <= 24 or is_raining:
    print("It's not a beautiful day") 

"""

"""""
temp = 39
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The event is canceled")
else:
    print("The even is on going")
"""""

"""""
temp = 24
is_sunny = False

if temp >= 28 and is_sunny:
    print("Its hot")
    print("Its sunny")

elif temp <= 0 and is_sunny:
    print("Its cold")
    print("Its sunny")

elif 28 > temp > 0 and is_sunny:
    print("Its warm outside")
    print("Its sunny")

elif temp >= 28 and not is_sunny:
    print("Its hot")
    print("Its not sunny")

elif temp <= 0 and not is_sunny:
    print("Its cold")
    print("Its not sunny")

elif 28 > temp > 0 and  not is_sunny:
    print("Its warm outside")
    print("Its not sunny")
"""""

"""""
# CONDITIONAL EXPRESSION = A one line shortcut for the if else statement (ternary opertator)

num = 8
a = 9
b = 7
age = 25

#print("Positive" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "Odd"
#max_num = a if a > b else b
#min_num = a if a < b else b
status = "Adult" if age >= 18 else "Not Adult"

#print(f"the max num is {max_num}")
#print(f"the min num is {min_num}")
print(f"Your are {status}")

"""""

"""""
a = 0.1
b = 6
c = 4

if a == b and b == c:
    print("All numbers are equal")
    max_num = a
elif a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

if a < b and a < c:
    min_num = a
elif b < a and b < c:
    min_num = b
elif c < a and c < b:
    min_num = c

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")

"""""

"""""
#STRING METHODS, built-in functions that can be used on strings to perform various operations
name = input("Enter your full name: ")

result = len(name)
spaces = name.find("e") or name.find("E")
rspaces = name.rfind("q") or name.rfind("Q")
other = name.upper().find("R")
result2 = name.isdigit() # checks if all characters in the string are digits only numbers
result3 = name.isalpha() # checks if all characters in the string are alphabetic


print(f"The result is {result}")
print(f"The spaces is {spaces}")
print(f"The rspaces is {rspaces}")
print(f"The other is {other}")
print(f"The result2 is {result2}")
print(f"The result3 is {result3}")

"""""

"""""
phone_number = input("Enter your phone number: ")

#phone_number = phone_number.count("-")
phone_number = phone_number.replace("-", "")


print(phone_number)
"""""

#print(help(str)) # prints the help for the str class

"""""
username = input("Enter your username: ")

if len(username) > 12:
    print("Username cant be longer than 12 characters")

spaces_username = username.count(" ") > 0

if spaces_username is True:
    print("Username cant have spaces")

elif username.isdigit():
    print("Username cant be numbers")

else:
    print("Username is valid")
"""""

"""""
#STRING METHODS
username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't be longer than 12 characters")
elif " " in username:
    print("Username can't have spaces")
#elif username.isdigit(): # checks if all characters in the string are digits only numbers
    #print("Username can't be numbers")
elif not username.isalpha(): # checks if all characters in the string are alphabetic
    print("Username can't have numbers")
else:
    print(f"Username is valid welcome {username}")
"""""

"""""
#INDEXING [START : END : STEP]

credit_number  = "1234-5678-9012-3456"

#print(credit_number[1])
#print(credit_number[0:3])
#print(credit_number[:3])
#print(credit_number[5:])
#print(credit_number[-1])
#print(credit_number[::2]) # prints every second character starting from the first
#print(credit_number[::-1]) # prints the string in reverse order

print(credit_number[15:19])

"""""

"""""
c_num = input("Enter your credit card number:  ")

if len(c_num) > 19:
    print("Invalid credit card number")

has_spaces = " " in c_num
if has_spaces is True:
    c_num = c_num.replace(" ", "-")
    print(c_num)
"""""

"""""
c_num = input("Enter your credit card number: ")
c_num = c_num.replace(" ", "").replace("-", "")  # Remove spaces and dashes

if not c_num.isdigit() or len(c_num) != 16: # Check if all characters are digits and length is 16
    print("Invalid credit card number. It must be exactly 16 digits.")
else:
    formatted = '-'.join([c_num[i:i+4] for i in range(0, 16, 4)]) # Format as XXXX-XXXX-XXXX-XXXX
    print(formatted)
"""""

"""""
c_num = "1234-5678-9012-3456"

#l_digits = c_num[-4:] # last 4 digits
#r_digits = c_num[:4] # first 4 digits
#m_digits = c_num[4:-4] # middle digits

#print(f"****-****-****-{l_digits}")
#print(f"{r_digits}-****-****-****")
#print(f"****{m_digits}****")


c_num = "1234-5678-9012-3456"
only_numbers = c_num.replace("-", "") # Remove dashes
print(only_numbers)

"""""

"""""

#FORMAT SPECIFIERS = {VALUE:FLAGS} format a valur based on what flags are inserted

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

#WHILE LOOPS

"""""
name = input("Enter your name: ")

while name == "":
    print("Please enter a name")
    name = input("Enter your name: ")
print(f"Welcome {name}")

"""""

"""""
age = int(input("Enter your age: "))

while age < 0:
    print("Please enter a valid age")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")
"""""

"""""
food = input("Enter your favorite food (q to quit): ")

while not food == "q":
    print(f"{food} is great")
    food = input("Enter your favorite food (q to quit): ")

print("Goodbye")
"""""

"""""
num = input("Enter a number between 1 and 10: ")




#while num < 1 or int(num) > 10:
   #print("Please enter a number between 1 and 10")

while not num.isdigit() or not (1 <= int(num) <= 10):
    print("Please enter a valid whole number between 1 and 10 (no decimals).")
    num = input("Enter a number between 1 and 10: ")

num = int(num)
print(f"Your number {num}")
"""""
#1:58:03

"""""
num = int(input("Enter a number between 1 and 10: "))

while int(num) < 1 or int(num) > 10:
    print("Please enter a number between 1 and 10")
    num = input("Enter a number between 1 and 10: ")

print(f"Your number {num}")
"""""

"""""
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {num}")
"""""

#INTEREST CALCULATOR WITH WHILE LOOPS
#1:59:45

"""""
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Principal amount must be greater than 0")
print(principle)

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("rate must be greater than 0")
print(rate)

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time must be greater than 0")

print(time)
print(f"Your interest rate is: {rate:.2f}%")
print(time) 

interest = principle * pow((1 + rate / 100), time)

total_amount = principle + interest

print(f"The interest is: ${interest}")
print(f"The total amount after {time} years is: ${total_amount:.2f}")

"""""

"""""
principle = 0
rate = 0
time = 0

while True: # Now its able to enter "0" 
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal amount must be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("rate must be greater than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time must be greater than 0")
    else:
        break

print(time)
print(f"Your interest rate is: {rate:.2f}%")
print(time) 

interest = principle * pow((1 + rate / 100), time)

total_amount = principle + interest

print(f"The interest is: ${interest}")
print(f"The total amount after {time} years is: ${total_amount:.2f}")
"""""

#FOR LOOPS, used to iterate over a sequence (list, tuple, string) or other iterable objects

"""""
for  x in range (1, 11):
    print(x)
"""""

"""""
for  x in reversed(range (1, 11)):
    print(x)

print("Happy New Year!")
"""""

"""""
credit_number  = "1234-5678-9012-3456" # iterate over each character in the string

for x in credit_number: # step of 2, counts by 2s
    print(x)
"""""

"""""
for x in range(1, 21): # iterate from 1 to 20
    if x == 13: 
        continue # skip the number 13, if changed by break it stops the loop at 13

    else:
        print(x)
"""""

#COUNTDOWN TIMER 

"""""
import time

my_time = int(input("Enter the time in seconds: ")) 

for x in range (0, my_time): # counts up from 0 to my_time
    print(x)
    time.sleep(1) # waits for 1 second 


print("times up!")
"""""

"""""

import time

my_time = int(input("Enter the time in seconds: ")) 

for x in reversed(range (0, my_time)): # counts down from my_time to 0 
    print(x)
    time.sleep(1) 

print("times up!")
"""""

"""""
import time

my_time = int(input("Enter the time in seconds: ")) 

for x in range (my_time, 0, -1): # counts down from my_time to 0
    
    seconds  = x  % 60
    minutes = int(x / 60) % 60
    hours = int(minutes / 60) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # :02 = adds a leading zero if seconds is less than 10
    time.sleep(1) 

print("times up!")

"""""

"""""
#NESTED LOOPS, a loop inside a loop

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):

    for y in range(columns): 
        print(symbol, end="") # end="" prevents new line after each symbol
    print()

"""""

#COLLECTIONS, data structures that can hold more than one value (list[], tuple(), set{}, dictionary)

#2:23:41

#sinay



