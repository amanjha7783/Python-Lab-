# 3) Write Python code to check whether the character or number is palindrome or not

# a = int(input("Enter the number : "))

# rev = 0
# temp = a
# while a != 0:
#     remainder = a%10 
#     rev = rev*10 + remainder
#     a = a//10

# if(temp == rev):
#     print(temp,"is a palindrome number ")
# else:
#     print(temp,"is not a palindrome number ")


def check_palindrome(a):
    
    if a == a[::-1]:
        print(a, "is a palindrome")
    else:
        print(a, "is not a palindrome")


a = input("Enter the character: ")
check_palindrome(a)
