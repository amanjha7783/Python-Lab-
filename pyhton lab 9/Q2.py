'''
2. Use filter to keep only even numbers from a list.
Input: [5, 10, 13, 20, 21] → Output: [10, 20]
'''

input_x = [5, 10, 13, 20, 21] 
output_x = list(filter(lambda x : x%2==0 , input_x))
print(output_x) 