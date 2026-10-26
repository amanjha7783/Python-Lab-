'''
10. String to dictionary
Write a Python program that counts how many times each character appears in a string
using a dictionary.
Input: "banana"
Output: {'b': 1, 'a': 3, 'n': 2}
'''

name = "banana"

no_count = {}
for char in name:
    if char in no_count:
        no_count[char] += 1
    else:
        no_count[char] = 1
print(no_count)