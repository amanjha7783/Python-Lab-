import numpy as np

a = np.empty((3, 4),dtype=int)
print("Empty array a:" )
print(a)
print("Type of array a:", type(a))
print("Size of array a:", a.size)
print("Shape of array a:", a.shape)
print("Dimensions of array a:", a.ndim)
print("Data type of array a:", a.dtype)
print("\n\n")

x = np.ones((2, 3),dtype=float)
print("Ones array x:" )
print(x)
print("\n\n")

y = np.zeros((4, 2),dtype=complex)
print("Zeros array y:" )
print(y)
print("\n\n")

z = np.full((2, 4), 7)
print("Full array z:" ) 
print(z)
print("\n\n")





