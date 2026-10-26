'''
1) Write a program that capitalizes every alternate character in a given string
Input: "hello world"
Output: "HeLlO WoRlD"
'''

str1 = input("Enter the string : ")

new_str = list(str1)
x = []
for i in range(len(new_str)):
    if(i%2 == 0):
        x.append(new_str[i].upper())
    else:
        x.append(new_str[i].lower())

print(''.join(x))