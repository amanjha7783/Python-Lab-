# Write a Python program to find the LCM (Least Common Multiple) and
#  GCD (Greatest Common Divisor) of two numbers using built-in functions.


def GCD(num1,num2):
    if(num1>num2):
        i = num2-1
        while i > 0:
            if(num1%i==0 and num2%i==0):
                break
            i=i-1 
    else:
        i = num1-1
        while i>0:
            if(num1%i==0 and num2%i==0):
                break
            i=i-1
    return i 

def LCM(num1 , num2):
    return (num1*num2)//GCD(num1,num2)
        
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

k = GCD(x,y)
print(f"Hcf of two number {x} and {y} is {k}")
print(f"Hcf of two number {x} and {y} is {LCM(x,y)}")



