#  find the Hcf of any two number 

x = int(input("enter the first number : "))
y = int(input("enter the second number : "))

if(x>y):
    i = y-1 
    while i >= 1:
        if(x%i == 0 and y%i == 0):
            print(f"HCF of {x} and {y} is {i}")
            break;
        i -= 1

else:
    i = x-1 
    while i >= 1:
        if(x%i == 0 and y%i == 0):
            print(f"HCF of {x} and {y} is {i}")
            break;
        i -= 1