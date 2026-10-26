'''
6) Write a program that takes two lists, one of keys and one of values, and creates a dictionary from them.
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
'''

keys_1 = ['name', 'age', 'city']
values_1 = ['Alice', 25, 'New York']

dict_1 = {}
for i in range(len(keys_1)):
    dict_1[keys_1[i]] = values_1[i]
print(dict_1)