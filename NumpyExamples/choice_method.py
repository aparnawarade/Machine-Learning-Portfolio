"""The choice() method allows you to generate a random value based on an array of values.

The choice() method takes an array as a parameter and randomly returns one of the values.
"""

x=random.choice([3,7,9])
print(x)

#put any of these numbers in x array of size (3,5)
x=random.choice([3,7,9,12],size=(2,5))
print(x)

x=random.choice([3,7,9,12],size=(5))
print(x)

"""
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0
"""
x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print("----1D array with choice fiunction and probability with size 100 ----")
print(x)
