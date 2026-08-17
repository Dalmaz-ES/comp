
capitals = {"USA": "Washington",
            "UK": "London",
            "RUS": "Moscow"}
"""
print("capitals:")
for x, y in capitals.items():
    print(x, y)
print()
"""


#print(dir(capitals)) to see different attributes of capitals
#print(help(capitals))

#TO FIND THE CAPITAL IF EXISTS IN DICTIONARY
"""
if capitals.get("USA"):
    print("Capital is in the dictionary")
else:
    print("That is not in the dictionary")
"""


#TO UPDATE OR CHANGE THE DICTIONARY
"""
capitals.update({"TR": "Ankara"})
print(capitals)
capitals.pop("RUS") # removes the key and value pair
capitals.popitem() # removes the last item
capitals.clear() # removes all items
capitals.keys() # returns the keys

keys = capitals.keys() # returns the keys and iterates over them
for key in capitals.keys():
    print(key)
    
capitals.values() # returns the values

for value in capitals.values(): # iterate over the values
    print(value)
    
capitals.items() # returns the key and value pairs

for key, value in capitals.items(): # iterate over the key and value pairs
    print(key, value)
"""


#TO FIND THE CAPITAL WHEN ENTERED THE COUNTRY
"""
country = input("Enter the Country: ").upper()
if country in capitals:
    print(f"The capital is {capitals[country]}")
else:
    print("That capital does not exist")
"""


