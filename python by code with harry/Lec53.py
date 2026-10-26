#  Map, filter , reduce

def cube(x):
    return x**3
def square(x):
    return x**2
list1 = [1, 2, 3, 4, 5]
newlist = []
for item in list1 :
    newlist.append(cube(item))
print(newlist)

newl = list(map(square, list1))
print(newl)

def filter_function(x):
    return x > 2

l = list(filter(filter_function, list1))
print(l)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)