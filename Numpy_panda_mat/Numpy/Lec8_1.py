import numpy as np

s1 = "MY name is Aman jha"
s2 = " I am from India "

x = np.char.add(s1,s2)  # concatenation of two strings
y = np.char.multiply(s2,3)  # repeat the string 3 times
print(x)
print(y)
print("\n")

a = np.char.lower(s1)   # convert to lowercase
b = np.char.upper(s2)   # convert to uppercase
c = np.char.split(s1)  # split the string
d = np.char.replace(s2,"India","USA")  # replace a substring with another substring
e = np.char.center(s1,50,'*')  # center the string with padding

print(a)
print(b)
print(c)
print(d)
print(e)
print("\n")

s4 = "Welcome to the world of Numpy"
g = np.char.find(s4,"world")  # find the index of substring
print(g)