
# LIST COMPREHENSIONS = a concise way to create lists
#                       compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

"""
doubles = []
for x in range(1, 11): #doubles number 1 to 10
    doubles.append(x * 2) #list comprh. ll be used to compact it

print(doubles)
"""
from selectors import SelectSelector

#compact version same as above
"""
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z ** 2 for z in range(1, 11)]

print(f" Double: {doubles}")
print()
print(f" Triple: {triples}")
print()
print(f" Square: {squares}")
"""


#strings
"""
fruits = ["apple", "banana", "orange"]

#fruit = [x.upper() for x in fruits]
fruit_char = [x[0] for x in fruits] #returns each 1st chrac of each fruit

print(fruit_char)
"""


#filtering
"""
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]

positive_numbers = [x for x in numbers if x > 0]
print(f"Positive numbers are: {positive_numbers}")

negative_numbers = [x for x in numbers if x < 0]
print(negative_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)
"""


#
"""
grades = [80, 90, 75, 60, 50, 100, 45, 15, 35]

passing_grades = [x for x in grades if x >= 50]
print(f"Passing grades are: {passing_grades}")
print()

not_passing_grades = [x for x in grades if x < 50]
print(not_passing_grades)
"""

