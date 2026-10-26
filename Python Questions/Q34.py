#  check the string is palindrom or not

str1 = input("Enter a string : ")
num = str1
lenght = len(str1)
print(lenght)
starting_length = -(lenght + 1)
print(starting_length)

reverse = str1[-1 : starting_length : -1]

print("After reversing the string is ",reverse)

if(num == reverse):
    print(num, "is palindrome string ")
else:
    print(num, "is not palindrome string ")


#  second method to check the string is palindrome or not
a = input("Enter a string : ")

rev = a[::-1]

if(a==rev):
    print(a, "is palindrome string ")
else:
    print(a, "is not palindrome string ")