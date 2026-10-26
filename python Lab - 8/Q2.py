'''
2) Write a program that counts how many times each word appears in a sentence and stores the result in a dictionary
Input: "apple banana apple mango banana apple"
Output: {'apple': 3, 'banana': 2, 'mango': 1}
'''

str1 = input("Enter the string : ")

dict1 = {}
words = str1.split() 
for word in words:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1
print(dict1)
