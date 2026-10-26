'''
7) Write a Python program to remove an empty tuple(s) from a list of tuples.
Input: [(), ('harsh',), (), ('x', 'y'), ('m', 'n', 'o'), ('p')]
Output: [('harsh',), ('x', 'y'), ('m', 'n', 'o'), 'p']-> tuple
'''

x = [(), ('harsh',), (), ('x', 'y'), ('m', 'n', 'o'), ('p')]
# Remove empty tuples from the list
x = [i for i in x if i != ()]
print(x) 