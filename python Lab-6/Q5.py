'''
5) Sort a tuple using first element tuple1 = (('b', 37),('c', 11),
('d',29),('a', 23)) -> tuple
'''

tuple1 = (('b', 37),('c', 11),('d',29),('a', 23))
list1 = list(tuple1)
# Sorting the list based on the first element of the tuple
list1.sort(key=lambda x: x[0])
tuple1 = tuple(list1)
print(tuple1)  
