import numpy as np
from numpy import random


"""
The randint() method 
takes a size parameter where you can specify the shape of an array.
"""

x = random.randint(100)

print(x)

#create 1 d array 
x=random.randint(100,size=(5))
print(x)

#create 2d Array 
x=random.randint(1,1001,size=(3,8))
print(x)

"""
Generate a floating poiunt array 
"""
#rand() method 
x=random.rand(5)
print(x)
#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x=random.rand(3,5)
print(x)
