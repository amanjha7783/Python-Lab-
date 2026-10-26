'''
12) Write a Python program using lambda to find all numbers in a list that are divisible by a
given number.
Example: Input: [10, 25, 30, 45, 50], Divisor: 5 → Output: [10, 25, 30, 45, 50]
'''

def find_divisible(numbers, divisor):
    return list(filter(lambda x: x % divisor == 0, numbers))


numbers = [10, 25, 30, 45, 50]
divisor = 5
print(find_divisible(numbers, divisor))  
