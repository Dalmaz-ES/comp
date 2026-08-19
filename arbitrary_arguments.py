
# ARBITRARY ARGUMENTS
# *args    (arguments)         = allows you to pass multiple non key arguments
# **kwargs (keyword arguments) = allows you to pass multiple keyword arguments
#                                * unpacking operator
#                                1.positional, 2.default, 3.keyword, 4.arbitrary


#args example
"""
def add(*args): # creates a tuple
    #print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5, 6))
"""

"""
#args example
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("LTD", "Eyip", "Sinay", "D.", "III.")
"""


#kwargs example
"""
def print_address(**kwargs): #packs them into a dictionary
    #print(type(kwargs))
#    for value in kwargs.values(): # prints all values in kwargs
#        print(value)

#    for key in kwargs.keys(): # prints all keys in kwargs
#        print(key)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Cetinay",
              city="Istanbul",
              state="Kartal",
              zip="34873",
              apt="23") # added a apt number
"""



#example using both

def shipping_label(*args, **kwargs): #args first
    for arg in args:                            #make sure kw arg follow positional arg
        print(arg, end=" ")
    print()

#    for value in kwargs.values(): #getting kwargs values
#        print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}") # ıf user does not have a apt it would display "None" unless used in IF
    elif "pobox" in kwargs: #added when changed "apt" with "pobox"
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}") # gets them on a separate line

shipping_label("Dr.", "Eyip", "Sinay", "D.", "III.",
               street="Cetinay",
               city="Istanbul",
               state="Kartal",
               zip="34873",
               pobox="PO box 1001") #"apt" removed and then changed w "pobox"

