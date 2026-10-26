def last_character(string):
    return string[-1]
print(last_character("Hello, World!"))

def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_even(10))

def greater_num(num1 , num2):
    if (num1 > num2):
        print(num1, "is greater than", num2)
    elif(num1 < num2):
        print(num2, "is greater than", num1)
    else:
        print(num1, "is equal to", num2)
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
greater_num(num1, num2)

def greatest(a,b,c):
    if a > b and a > c:
        print(a,"is gretaest number")
    elif(b>c and b>a):
        print(b,"is greatest number")
    elif(c>a and c>b):
        print(c,"is greatest number")
    else:
        print("all numbers are equal")

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

greatest(a,b,c)