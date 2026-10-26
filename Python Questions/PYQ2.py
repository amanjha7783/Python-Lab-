# def has_duplicate_letters(sentence):
#     words = sentence.split()  # Split sentence into words
#     for word in words:
#         seen_letters = set()
#         for letter in word:
#             if letter in seen_letters:
#                 return True  # Found a duplicate letter in a word
#             seen_letters.add(letter)
#     return False  # No duplicate letters found in any word

# # Example Usage
# print(has_duplicate_letters("hello world"))  # True (hello has duplicate 'l')
# print(has_duplicate_letters("abc def ghi"))  # False (no duplicate letters)
# print(has_duplicate_letters("apple banana orange"))  # True (apple has duplicate 'p')


# write a program that accepts a sentence and calculate the number of vowels, 
# digits, uppercase and lowercase letters.

def count_vowel(n):
    vowels = "aeiou"
    count = 0
    for i in n.lower():
        if i in vowels:
            count += 1
    return count

x = count_vowel("elephant")    
print(x)

def count_upper_case(n):
    count = 0
    for i in n:
        if (i == i.upper() ):
            count += 1
    return count

x = count_upper_case("ElephAnt")    
print(x)

def count_Lower_case(n):
    count = 0
    for i in n:
        if (i == i.lower()):
            count += 1
    return count

x = count_Lower_case("ElephAnt")    
print(x)