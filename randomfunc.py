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
