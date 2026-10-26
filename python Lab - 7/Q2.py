'''
2. Dictionary Operations
Write a program that takes a string as input and creates a dictionary where:
● The keys are unique characters in the string.
● The values are the number of times each character appears.
'''

string_x = input("Enter the string : ")

letter_count = {}
for letter in string_x:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
        
print(letter_count)