x=np.array([1,2,3,4])
y=np.array([5,7,8,9])

z= np.sum([x,y])
print("SUm of add to one value : ",z)

z=np.add(x,y)
print("Addition of each dimention element : ",z)

z=np.subtract(x,y)
print("substraction : ",z)

z=np.multiply(x,y)
print("Multiplication : ",z)

z=np.divide(x,y)
print("Divide : ",z)

z=np.power(y,x)
print("Power of: ",z)

z=np.mod(x,y)
print("MOd of : ",z)

z=np.remainder(x,y)
print("Remonder of : ",z)
"""
Quotient and Mod
The divmod() function return both the quotient and the the mod. 
The return value is two arrays, 
the first array contains the quotient and second array contains the mod.
"""
z=np.divmod(x,y)
print("divmod of : ",z)

arr=np.array([-1,1,-2,-3])
print("Absolute of : ",np.absolute(arr))

