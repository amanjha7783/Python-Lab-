'''
13) Write a Python program using map() and lambda to convert a list of strings to uppercase.
Example: Input: ['hello', 'world'] → Output: ['HELLO', 'WORLD']
'''

def capitalized(strings):
    return list(map(lambda x: x.upper(), strings))

string_1 = ['hello', 'world']
print(capitalized(string_1))