'''
5) Write a program that finds the keys that are in one dictionary but not the other.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
Output: {'a', 'd'}
'''

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

for key in dict1:
    if key not in dict2:
        print(key, end=' ')
for key in dict2:
    if key not in dict1:
        print(key, end=' ')
