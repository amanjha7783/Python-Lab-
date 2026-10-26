#  WAP to verify whether x^3+x is less than or equal to 3x for a given value of x. (take input from 
# user)

x = int(input("Enter the value of x: "))

a = (x**3)+x
b = 3*x

if (a>b):
    print(f"{a} is greater than {b}")
    print("Hence proved  x^3+x is less than or equal to 3x for a given value of x ")
else:
    print(f"{b} is greater than {a}")


