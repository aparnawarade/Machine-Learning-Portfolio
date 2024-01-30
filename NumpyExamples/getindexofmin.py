"""
Write a Python program using NumPy to create a 10x10
matrix filled with random integers between 1 and 100. 
Find the minimum and maximum values of the matrix along with their indices.
"""

import numpy as np 
arr=np.random.randint(1,100,size=(20,20))
print(f"Minimum value is :{np.min(arr)} is at index {np.unravel_index(np.argmin(arr), arr.shape)}")
print(f"Maxium value is :{np.max(arr)} is at index {np.unravel_index(np.argmax(arr), arr.shape)}")

