

"""
my_list = [1, 2, 3, 2, 1, 4, 5, 4]


result = []
[result.append(item) for item in my_list if item not in result]


print("Original list:", my_list)
print("List after removing duplicates:", result)

"""


user_input = input("Enter a list of numbers separated by spaces: ") 


unique_numbers = [] 
seen = set()
unique_numbers = [x for x in map(int, user_input.split()) if not (x in seen or seen.add(x))]

print("List after removing duplicates:", unique_numbers)