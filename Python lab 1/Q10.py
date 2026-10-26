'''
 Write a program to print Fibonacci series up to n numbers where n will be taken as input. 
Hint: The Fibonacci series is 0,1,1,2,3,5,8,13… where first term is 0, second term is 1 and the n-th term 
is the sum of (n-1)-th term and (n-2)-th term for all n >= 3.
'''

def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a number: "))
for i in range(n+1):
    print(f"{fibonacci(i)}", end=" ")  