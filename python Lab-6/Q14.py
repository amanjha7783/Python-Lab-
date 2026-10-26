'''
Use map() and lambda to calculate the square root of numbers in a list.
Example:
Input: [4, 16, 25, 36]
Output: [2.0, 4.0, 5.0, 6.0]
'''

def square(num):
    return list(map(lambda x : x**(1/2), num))

number = [4,16,25,36]
print(square(number))


