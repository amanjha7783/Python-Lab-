'''
8. Write a program that:
● Takes a list of words as input.
● Converts each word to uppercase using map().
● Filters out words that have more than 5 letters using filter().
● Concatenates the remaining words into a single string using reduce().
Input: ["apple", "banana", "cat", "dog", "elephant"]
Output: "CATDOG"
'''

name = ["apple", "banana", "cat", "dog", "elephant"]

x = []

for i in range(len(name)):
    if len(name[i]) < 5:
        x.append(name[i].upper())

print(''.join(x))


        