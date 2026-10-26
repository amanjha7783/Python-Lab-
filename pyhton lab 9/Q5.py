'''
Use filter to extract words with length > 5 from a list.
Input: ["apple", "banana", "kiwi", "pineapple"] → Output: ["banana", "pineapple"]
'''

input_x = ["apple", "banana", "kiwi", "pineapple"]
output_x = list(filter(lambda X: len(X) > 5, input_x))
print(output_x)