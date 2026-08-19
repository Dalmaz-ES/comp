
#FUNCTIONS = a block of reusable code
#            place () after the function name to invoke it
"""
def happy_birthday(name, age): #order matters
    print(f"Happy Birthday to {name}")
    print(f"You are this old {age}")
    print("Happy birthday to you")
    print()

happy_birthday("sinay", 18) #as in the order of defined
happy_birthday("as", 19)
happy_birthday("dt", 20)
"""

#ANOTHER EXAMPLE
"""
def display_invoice(username, amount, due_date):
    print(f"Hello {username} you have paid £{amount:.2f} for this date {due_date}")

display_invoice("Sinay", 52.599, "12/10/26")
"""


#RETURNS = statements used to end a function
#          and send a result back to the caller
"""
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

#print(add(1, 2))
#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divide(1, 2))

x = float(input("Enter x: ")) # x and y are variables to get input rather then print(add(1, 2))
y = float(input("Enter y: "))
print()

print(f"Addition is {add(x, y):.2f}")
print(f"Subtraction is {subtract(x, y):.2f}")
print(f"Multiplication is {multiply(x, y):.2f}")
print(f"Division is {divide(x, y):.3f}")
"""


#RETURN MAME CREATION
"""
def create_name(first, last):
    full_name = f"{first} {last}".capitalize()
    return full_name

print(create_name("eyip", "sinay"))


#Also can be written like
#def create_name(first, last):
#   first = first.capitalize()
#   last = last.capitalize()
#   return first + " " + last
#print(create_name("eyip", "sinay")
"""


