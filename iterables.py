
#ITERABLES = an object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

#lists and tuples
"""
numbers = [1, 2, 3, 4, 5] #lists and tuples are iterable

for number in numbers:
    print(number)
"""


#sets
"""
fruits = {"apple", "orange", "banana", "coconut"} #sets are unordered, unchangeable, and unindexed
for fruit in fruits:                              #sets are unreversible
    print(fruit)
"""

#strings
"""
name = "John Doe"

for character in name:
    print(character, end=" ")
"""


#dictionaries

my_dict = {"A":1, "B":2, "C":3} #dict return keys not values unles used .values()
                                #if needed both use items method
for x, y in my_dict.items():
    print(f"{x} = {y}")
    #print(x, y)

