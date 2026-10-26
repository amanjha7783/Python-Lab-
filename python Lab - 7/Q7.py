'''
Q7) Write a Python program that uses reduce() to find the product of all elements in a list.
Input: [1, 2, 3, 4, 5]
Output: 120 # (1*2*3*4*5)
'''


from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)