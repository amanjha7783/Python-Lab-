import numpy as np

a = np.arange(1,11).reshape(2,5)
b = np.arange(21,31).reshape(2,5)

print(a)
print("\n")
print(b)
print("\n")

print("sum of a and b is ")
print(a+b)
print("\n")

print("subtract of a and b is ")
print(b-a)
print("\n")

print("Multiplication of a and b is ")  # not my mtarice multiplication
print(a*b)
print("\n")

print("Division of a and b is ")
print(b/a)
print("\n")

x = np.arange(0,18).reshape(6,3)
y = np.arange(20,38).reshape(3,6)

print(x)
print("\n")
print(y)
print("\n")

print("Dot product of a and b")
print(x.dot(y))
print("\n")

print("Maximum number is ", y.max())
print("Minimum number is ", y.min())
print("Minimum element index is ", x.argmax())