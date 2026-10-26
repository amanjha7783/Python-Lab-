'''
Sort a tuple using second element tuple1 = (('b', 37),('c', 11),
('d',29),('a', 23)) - tuple
Input: (('x', 25), ('y', 50), ('z', 18), ('w', 33))
Output: (('z', 18), ('x', 25), ('w', 33), ('y', 50))
'''

tuple1 = (('x', 25), ('y', 50), ('z', 18), ('w', 33))

list1 = list(tuple1)
list1.sort(key= lambda x:x[1])
tuple1 = tuple(list1)
print(tuple1)