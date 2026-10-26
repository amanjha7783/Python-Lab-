import numpy as np

a = np.arange(3, 21, 2)
print("Arange array a:" )
print(a)
print("\n\n")

a = a.reshape(3, 3)
print("Reshaped array a to 3x3:" )
print(a)
print("\n\n")

b = a.flatten()
print("Flattened array b from a:" )
print(b)
print("\n\n")

c = a.ravel()
print("Raveled array c from a:" )
print(c)
print("\n\n")

#difference between flatten and ravel
# flatten returns a copy, ravel returns a view (if possible) of the original array 
# so changes to ravelled array may affect the original array but changes to flattened array will not affect the original array 
# ravel is more memory efficient as it does not create a copy unless necessary