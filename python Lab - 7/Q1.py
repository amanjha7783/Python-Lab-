'''
1. String Manipulation
Write a Python program that takes a sentence as input and:
● Converts it to lowercase.
● Removes all vowels (a, e, i, o, u).
● Reverses the string.
'''


sentence_1 = input("Enter the string : ")
print(f"after lower the string is {sentence_1.lower()}")

def remove_vowel(x):
    vowels = 'aeiou'
    return ''.join([letter for letter in x if letter not in vowels])

y = remove_vowel(sentence_1.lower())
print(f"after removing vowels: {y}")

z = list(y)
z.sort(reverse=True)
result = ''.join(z)
print(f" after revrse the string is {result}")


# p = z.sort(reverse = True)
# print(p) 