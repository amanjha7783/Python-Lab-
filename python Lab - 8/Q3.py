'''
3) Write a program that finds the first character in a string that does not repeat.
Input: "swiss"
Output: "w"
'''

str1 = input("Enter the string : ")

new_str= list(str1)
for i in range(len(new_str)):
    if new_str.count(new_str[i]) == 1:
        print(new_str[i])
        break