'''
WAP to find out the highest common factor (HCF) of two given positive integers n and m. Then 
use HCF of n and m to find the least common multiple (LCM) of n and m. 
'''

m = int(input("Enter the first number is : "))
n = int(input("Enter the second number is : "))

if(m>n):
    i = n-1 
    while i >= 1:
        if(m%i == 0 and n%i == 0):
            hcf = i
            print(f"HCF of {m} and {n} is {i}")
            break;
        i -= 1
else:
    i = m-1 
    while i >= 1:
        if(m%i == 0 and n%i == 0):
            hcf = i
            print(f"HCF of {m} and {n} is {i}")
            break;
        i -= 1 

Lcm = (m*n)/hcf
print(f"LCM of {m} and {n} is {Lcm}")


