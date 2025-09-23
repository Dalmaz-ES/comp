"""
def hello():
    print("Hello")
    print("Hello Again")

print("my name is sinay")
for i in range(5):
    hello()
"""

"""
def hello(name):
    print("Hello"+name)
    print("Hello Again")

print("my name is sinay")
for i in range(5):
    hello(str(i))
"""

"""""
def square(x):
    a = 5
    return(x*x*a)

print(square(5))
print(x) # Removed the print(x) line since x is not defined in the global scope
for i in range(square(3)):
    print("Hi")
"""""

"""
def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(remove_duplicates(my_list))  
"""

"""
def triangle_area(x,y):
    return x*y/2
print(triangle_area(5,6))
"""

"""
def triangle_area(x, y):
    return x * y / 2

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)

print(f"The area of the triangle is: {area}")
"""

"""
def triangle_area(base, height):
    return base * height / 2

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

print("The area of the triangle is:", triangle_area(base, height))
"""

"""
def average(total_sum, count):
    return total_sum / count

total_sum = 10
count = 2
print(average(total_sum,count))
"""


def average(numbers):
    return sum(numbers) / len(numbers) 

numbers = list(map(int, input("Enter the numbers separated by space: ").split())) 
print(average(numbers))
