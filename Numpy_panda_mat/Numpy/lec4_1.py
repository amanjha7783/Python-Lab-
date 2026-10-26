import numpy as np

a = np.arange(1,101)
a = a.reshape(10,10)

print("Array a (10x10):")
print(a)
print("\n\n")

# silicing

print(a[0])  # first row
print("\n")
print(a[2:6])  # rows 2 to 5
print("\n")
print(a[2,6])  # 2nd row, 6th column
print("\n")
print(a[:,5])  # all rows, 5th column
print("\n")
print(a[2:8, 2])  # rows 2 to 7, 2nd column
print("\n")
print(a[2, 2:8])  # 2nd row, columns 2 to 7
print("\n")

print("Sliced array (rows 2 to 5 and columns 3 to 7):")
sliced_a = a[2:6, 3:8]
print(sliced_a)