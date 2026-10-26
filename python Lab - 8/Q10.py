'''
10) Write a program that calculates the factorial of a number using reduce().
Input: 5
Output: 120  # (5*4*3*2*1)
'''

from functools import reduce

num = int(input("Enter a number: "))

fact  = reduce(lambda x, y: x * y, range(1, num + 1))
print(fact)
