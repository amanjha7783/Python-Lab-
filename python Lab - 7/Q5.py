'''
Q5) Write a Python program that takes a list of integers and uses map() to return a list of
squares of those numbers.'
'''

numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(lambda x: x**2, numbers))
print(square_numbers)

