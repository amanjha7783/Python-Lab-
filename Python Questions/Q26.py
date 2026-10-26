# Find the Highest factor of any number 

n = int(input("enter the number : "))
i = n-1 
while i >= 1:
    if(n%i == 0):
        print(f"HCF of {n} is {i}")
        break;
    i -= 1
    