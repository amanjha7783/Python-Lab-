'''
Write a python program to find the value of the following expression 
1+X+X^2/2! +X^3/3! +...+X^n/n! for the given values of X (float) and n (integer). 
Note that ^ is used for an exponential operator, not for "bitwise XOR"
'''

def facotial(n):
    if(n<=1):
        return 1
    else:
        return n*facotial(n-1)

def expression(n):
    sum = 1
    for i in range(n):
        sum = sum + (n**i)/facotial(i)
        # print(sum)
    print(sum)
n = int(input("Enter the value of n: "))
expression(n)