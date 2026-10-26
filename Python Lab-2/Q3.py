'''
Write a Python program to find the product of every two consecutive positive integers up 
to a given positive integer N.
'''

def product_of_consecutive_integers(n):
    for i in range(1,n+1):
        print(f"product of {i} and {i+1} is {i * (i+1)}")

n = int(input("Enter the number : "))
x = product_of_consecutive_integers(n)
print(x)

