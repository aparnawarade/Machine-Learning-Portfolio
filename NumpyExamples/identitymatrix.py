"""
Using NumPy, create a 5x5 identity matrix 
 

Print the resulting vector.
"""
import numpy as np 

arr=np.identity(5)
print(arr)

#and add a scalar value of 5 to it. 
newarr=arr+5
print(newarr)

#column vector filled with random integers between 1 and 10
arr_column=np.random.randint(1,10,size=(5,1))
print(arr_column)

#Multiply the resulting matrix with a 5x1
result=np.multiply(newarr,arr_column)
print("rESULTING mATRIX IS :\n ",result)
