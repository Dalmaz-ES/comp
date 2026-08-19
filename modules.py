
# MODULE = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up large program reusable separate files


# print(help("modules")) #shows all built-in modules
# similarly replace with a module to see its documentation

#import math

#import math as m
#print(m.pi)

#from math import pi
#print(pi)

"""
from math import e

a, b, c, d, e= 1, 2, 3, 4, 5 #when using a module, try not to use
print(e ** a)                #the same module name in different variables
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)
"""



#write it like this to overcome the above problem
"""

import math
a, b, c, d, e= 1, 2, 3, 4, 5 #fixed version
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
"""


pi = 3.14159

def square(x):
    return x ** 2

def cude(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2
