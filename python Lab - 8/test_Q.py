'''
Question 1: Text Data Processing
Write a Python program that:

Takes a string input from the user.

Converts the string to lowercase.

Creates a dictionary where keys are unique characters and values are their counts.

Removes all vowels (a, e, i, o, u) from the string.

Uses filter() to keep only consonants in the modified string.

Uses reduce() to concatenate the remaining characters into a single string.

'''
#  first part
str1 = "Hello World"
print(str1.lower())

#  second part
dict1 = {}
for char in str1.lower():
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

print(dict1)

#  third part
vowel = "aieou"
new_str = list(str1)
for char in str1:
    if char.lower() in vowel:
        new_str.remove(char)
print(''.join(new_str))

# fourth part
vowels = "aeiou"
new_str = list(filter(lambda x: x.lower() not in vowels, str1))
print(new_str)

# fifth part
from functools import reduce
print(reduce(lambda x, y: x + y, new_str))


