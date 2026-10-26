import numpy as np

x = np.arange(0,18).reshape(6,3)
y = np.arange(20,38).reshape(6,3)

print("Sum of array is " , x.sum())
print("Sum of array is " , np.sum(x, axis=0)) # sum of each column 
print("Sum of array is " , np.sum(x, axis=1)) # sum of each row 1st row , 2nd row, 3rd row sum
print("\n")

print("Mean of array", np.mean(y))
print("\n")

print("square root of each element in array", np.sqrt(y))
print("\n")
print("LOg of each element in array", np.log(y))
print("\n")

print("standard deviation of array", np.std(y))
print("\n")