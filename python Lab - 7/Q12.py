'''
12. Invert dictionary(Swap keys and values)
Write a program that swaps keys and values in a dictionary.
Input: {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}
'''

original = {'a': 1, 'b': 2, 'c': 3}

inverted = {value: key for key, value in original.items()}

print(inverted)

