'''
2) Write a program that takes a user-inputted string, converts lowercase to uppercase,
removes question marks and exclamation marks, and prints the result. - STRING
Input: "Hello, World! How are you?"
Output: "HELLO WORLD HOW ARE YOU"
'''

str = input("Enter the string : ").upper()
str1 = str.replace("?","")
str2 = str1.replace(",", "")
new_str = str2.replace("!", "")
print(new_str)
