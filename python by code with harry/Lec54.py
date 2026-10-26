# The (is) operator compares the identity of two objects,
#  while the == operator compares the values of the objects.
#  This means that is will only return True if the objects 
# being compared are the exact same object in memory,  
# while == will return True if the objects have the same value.

a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True


a = 5
b = 5
print(a == b)  # True
print(a is b)  # True

# One important thing to note is that, in Python, 
# strings and integers are (immutable), which means that once they are created,
#  their value cannot be changed. This means that, for strings and integers,
#  is and == will always return the same result:

list1 = [2,3,4,5,6]
list2 = [2,3,4,5,6]
print(list1 is list2) # False
print(list1 == list2) # True 
# For (mutable) objects such as lists and dictionaries, is and == can behave differently.
#  In general, you should use == when you want to compare the values of two objects, 
# and use is when you want to check if two objects are the same object in memory.

x = 4
y = '4'
print(x is y) # False
print(x == y) # False