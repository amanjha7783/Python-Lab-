
import numpy as np


lst = [1, 2, 3, 4, 5]
print(lst)
print("Type of list:", type(lst))
print("\n\n")


print("1D array:")
a = np.array(lst)
print(a)
print("Type of list a:", type(a))
print("Size of array a:", a.size)
print("Shape of array a:", a.shape)
print("Dimensions of array a:", a.ndim)
print("Data type of array a:", a.dtype)
print("\n\n")

print("2D array:")
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)
print("Type of list b:", type(b))
print("Size of array b:", b.size)
print("Shape of array b:", b.shape)
print("Dimensions of array b:", b.ndim)
print("Data type of array b:", b.dtype)
print("\n\n")

print("3D array:")
c = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8.2, 9]]])
print(c)
print("Type of list c:", type(c))
print("Size of array c:", c.size)
print("Shape of array c:", c.shape)
print("Dimensions of array c:", c.ndim)
print("Data type of array c:", c.dtype)
print("\n\n")

print("Transpose of 2D array b:")
print(b.T)
print("\n\n")