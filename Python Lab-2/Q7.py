'''
Write a program in Python to print all the prime number less than a given positive integer 
N. Note that you may need to use nested-for loop.
'''

def prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                print(i)
                break

x = int(input("Enter a positive integer: "))
print(prime(x),end=" ")



