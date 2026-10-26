#  check the number is palindrome or not 

str1 = int(input("Enter a number : "))

length = len(str(str1))
print("Length of number is ",length)
reverse = 0
num = str1
for i in range(length):
    rem = str1%10  
    reverse = reverse*10 + rem
    str1 = str1//10

print("After reversing the number is ",reverse)

if(num == reverse):
    print(num, "is palindrome number ")
else:
    print(num, "is not palindrome number ")
