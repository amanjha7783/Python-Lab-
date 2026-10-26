'''
Write a program that uses filter() to find all numbers in a list that are divisible by 3
Input: [1, 3, 4, 6, 9, 12, 15]
Output: [3, 6, 9, 12, 15]
'''

numbers = [1, 3, 4, 6, 9, 12, 15]
divisible_by_3 = list(filter(lambda x : x%3==0, numbers))
print(divisible_by_3) 