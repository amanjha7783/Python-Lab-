'''
 A 4-digit number is entered through keyboard. Write a program to print a new number with digits 
reversed as of original one.
'''
def reverse_number(n):
    print(n[::-1])
        
n = input("Enter a 4-digit number: ")
if (len(n) == 4):
    reverse_number(n)
else:
    print("Invalid input. Please enter a non-negative integer.")
        
        