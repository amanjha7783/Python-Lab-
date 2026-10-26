'''
7) Write a program that takes a list of temperatures in Celsius and converts them to Fahrenheit using map().
Input: [0, 20, 37, 100]
Output: [32.0, 68.0, 98.6, 212.0]
'''

input_1 = [0, 20, 37, 100]

output_1 = list(map(lambda x : (x * 9/5) + 32, input_1))
print(output_1) 