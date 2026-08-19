
# KEYWORD ARGUMENTS = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments does not matter
#                     1.positional, 2. default, 3.keyword, 4.arbitrary

"""
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr", first="eyip", last="sinay") #positional arguments are first
"""

"""
for x in range(1, 11):
    print(x, end=" ") # keyword argument with space
"""

"""
print("1", "2", "3", "4", "5", sep="-") #seperates with a dash
"""


#EXERCISE GENERATE PHONE NUMBER
"""
def phone_number(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

x = phone_number(country=90, area=543, first=664, last=8482)

print(x)
"""
