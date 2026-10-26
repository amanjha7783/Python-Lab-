'''
A numeric palindrome is a number which remains the same even when you reverse the 
digits of the given number, e.g., 121, 34543, 6776, etc. Write a Python program to check a 
given positive number is a numeric palindrome or not.
'''
def is_palindrome(num):
    temp = num
    reverse = 0
    for i in range(len(str(num))):
        remainder = num%10
        reverse = reverse*10 + remainder
        num = num//10

    if (temp == reverse):
        print(f"{temp} is a numeric palindrome")
    else:
        print(f"{temp} is not a numeric palindrome")

number = int(input("Enter the number :"))
is_palindrome(number)
        