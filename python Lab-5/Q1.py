# Q1) Write a program to reverse a given string without using slicing ([::-1]).

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str 
    return reversed_str

input_str = input("Enter the string: ") 
print("Reversed string:", reverse_string(input_str))
