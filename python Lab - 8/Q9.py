'''
9) Write a program that finds the longest word from a list of words using reduce().
Input: ["apple", "banana", "strawberry", "fig"]
Output: "strawberry"
'''

input_1 = ["apple", "banana", "strawberry", "fig"]
longest_word = ""
for word in input_1:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word) 