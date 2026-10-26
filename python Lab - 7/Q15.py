'''
15 Write a program that filters even and odd numbers from a list using filter()
Input: [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 3, 5, 7]
'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)
