import numpy as np
 
a = np.random.random(2)
b = np.random.random((5,3))  # Random 5x3 array
c = np.random.randint(1,10)  # Random integer between 1 and 10Random integer between 1 and 10
d =  np.random.randint(1,10,(2,2))
e =  np.random.randint(1,10,(3,4,5))
print(a)
print("\n")
print(b)
print("\n")
print("Random integer between 1 and 10 ",c)
print("\n")
print(d)
print("\n")
print(e)
print("\n")



x = np.random.rand(2,2)
print(x)
print("\n")
y = np.random.randn(2,2) # negative and positive values both
print(y)
print("\n")


p = np.arange(1,10)
print(p)
print("\n")
print(np.random.choice(p,3))  # choose 3 random values from array p
print("\n")