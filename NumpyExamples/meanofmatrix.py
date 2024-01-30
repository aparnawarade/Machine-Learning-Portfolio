"""
Write a Python program using NumPy to create a 5x5 matrix filled with random integers between 1 and 100.
Calculate the mean and standard deviation of the matrix and print them.
"""
import numpy as np 
from numpy import random

arr=random.randint(1,100,size=(5,5),dtype='int')
print(arr)
#mean means addition of all the eelement of matrix /no of elemnets 
print("Mean is : ",np.mean(arr))
#avg of : standard devation is squares of all the numbers-mean 
print("standard devation is ",np.std(arr))
