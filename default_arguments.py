
#DEFAULT ARGUMENTS = a default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1.position, 2.default, 3.keyword, 4.arbitrary
"""
def net_price(list_price, discount=0, tax=0.05): #some are always the same value like tax,
    return list_price * (1 - discount) * (1 + tax) #so u use default value

#print(net_price(500)) # discount and tax are default so its written like this

#print(net_price(500, 0.1))

#print(net_price(500, 0.1, 0))
"""


#COUNT UP TIMER
"""
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Times Up")

count(5, 2)
"""
