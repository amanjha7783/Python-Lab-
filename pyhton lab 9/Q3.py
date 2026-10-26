'''
Use reduce to compute the product of all numbers in a list.
Input: [1, 2, 3, 4] → Output: 24
'''

from functools import reduce
input_x = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, input_x, 1)  
print(result)