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



temp = float(input("Enter the temperature: ") )
is_raining = True


if temp >= 25 and not is_raining:
    print("It's a beautiful day") 
elif temp <= 24 or is_raining:
    print("It's not a beautiful day") 


