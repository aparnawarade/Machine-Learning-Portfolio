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
