'''
8) Write a program that filters out words containing the letter 'e' from a list of words using filter().
Input: ["apple", "banana", "cherry", "date", "fig"]
Output: ["banana", "fig"]
'''

input_1 = ["apple", "banana", "cherry", "date", "fig"]
for word in input_1:
    if 'e' not in word:
        print(word)