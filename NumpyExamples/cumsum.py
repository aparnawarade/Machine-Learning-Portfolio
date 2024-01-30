"""
Using NumPy, create a 1000-element array of random integers between 1 and 1000.
Calculate the cumulative sum of the array 
and print the 10th, 100th, and 500th elements of the cumulative sum array.
"""
import numpy as np 
arr=np.random.randint(1,1000,1000)
result=np.cumsum(arr)
print("10th Element: ",result[9])
print("100th Element: ",result[99])
print("500th Element: ",result[499])
