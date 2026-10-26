'''
11) Write a Python program to find the key with the maximum value in a dictionary. 
'''

data = {'a': 10, 'b': 50, 'c': 30}

max_key = max(data, key=data.get)
print(max_key) 
