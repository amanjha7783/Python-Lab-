# Write a program that takes a sentence as input and:

# Counts the number of words.
# Replaces all spaces with underscores _.
# Finds the most frequent letter.


sentence = input("Enter the sentence : ")

words = sentence.split()
print("Number of words in the sentence:", len(words))

print(sentence.replace(" ","_"))

A = []
for char in sentence:
    if char.isalpha():
        A.append(char)

print("Most frequent letter in the sentence:", max(set(A), key=A.count))





