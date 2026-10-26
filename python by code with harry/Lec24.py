# Tuples in python

tuple = (1,4,7, "Green", True)
print(tuple)
print(tuple[0])
print(tuple[3])
print(tuple[4])
print(tuple[-2])

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 3421 is present in this tuple")
else:
  print("No 3421 is not present in this tuple")
tup2 = tup[1:4]
print(tup2)