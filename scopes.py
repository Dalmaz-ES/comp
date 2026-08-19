
# VARIABLE SCOPE = where a variable is visible a accessible
#
# SCOPE RESOLUTION ORDER = (LEGB) local -> Enclosed -> Global -> Built-in
#

"""
def func1(): #functions can't access variables outside of them
    a = 1    #if you change a to b, func2() won't work
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()
"""

#local scope
"""
def func1(): #2 local versions of x
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
"""


#enclosed scope
"""
def func1(): #uses previous x because it did not found in func2
    x = 1

    def func2():
        print(x)
    func2()
func1()
"""


#global scope
"""
def func1():
    print(x)

def func2():
    print(x)

x = 1
func1()
func2()
"""


#built-in scope

from math import e #built-in version of e
def func1():
    print(e)

e = 3 #global version of e
func1()
