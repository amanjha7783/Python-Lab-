# operations on tuple

tuple1 = (4, 5, "yellow", True)
tuple2 = (6, 7, "Blue", False)

tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple1.count(5)) # count the number of 5 in tuple1
print(tuple3.index(7)) # returns the index of the first occurrence of the specified value