'''
 Write a Python program to print a multiplication table of any given positive integer N (up 
to N * 10 =?)
'''

def print_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1,11):
        print(f"{n} * {i} = {n * i}")

n = int(input("Enter the number: "))
print_table(n)