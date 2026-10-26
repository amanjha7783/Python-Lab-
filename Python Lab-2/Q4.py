'''
Write a Python program to print all the digits of a given positive integer N.
'''

number = list(input("Enter the number : "))
for i in range(len(number) ):
    print(f"{number[i]}",end = " ")