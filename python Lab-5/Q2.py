# Write a function to check whether a given string is a palindrome.

def check_palindrome(n):
    if(n == n[::-1]):
        print(f"{n} is plaindrome")
    else:
        print(f"{n} is not a plaindrome")

x = input("Enter the input : ")
check_palindrome(x)