'''
Use map to convert a list of strings to uppercase.
Input: ["hello", "world"] → Output: ["HELLO", "WORLD"]
'''

input_x = ["hello", "world"] 
output_x = list(map(lambda x : x.upper(), input_x))
print(output_x)