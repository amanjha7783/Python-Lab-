def palindrome(num):
    temp = num
    x = num[-1::-1]
    if x == temp:
        print(temp , "is a palindrome")
    else:
        print(temp , "is not a palindrome")

num = input("Enter the string : ")
palindrome(num)

def fibo(a):
        if (a<=1):
            return a
        else:
            return (fibo(a-1) + fibo(a-2))
        
a = int(input("Enter the number : "))
i = 0
while i <= a:
    print(fibo(i))
    i += 1

