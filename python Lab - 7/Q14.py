'''
14 Write a program that filters prime numbers from a list using filter()
Input: [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 3, 5, 7]
'''

numbers  = [2, 3, 4, 5, 6, 7, 8, 9, 10] 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(is_prime, numbers))
print(filtered_numbers)