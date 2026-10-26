'''
11. merge dictionary
Write a program that merges two dictionaries by adding values of common keys.
x = {'a': 10, 'b': 20}
y= {'b': 30, 'c': 40}
Z= {'a': 10, 'b': 50, 'c': 40}
'''



x = {'a': 10, 'b': 20}
y = {'b': 30, 'c': 40}

for key , value in y.items():
    if key in x.keys():
        x[key] = x[key] + y[key]
    else:
        x[key] = y[key]

print(x) 