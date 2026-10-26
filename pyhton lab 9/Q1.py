'''
1. Use map to square each number in a list.
Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]z
'''

input_x = [1, 2, 3, 4]
output_x = list(map(lambda x : x**2, input_x))
print(output_x)