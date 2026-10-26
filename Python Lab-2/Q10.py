'''
Write a program to convert a binary number to a decimal number without using built-in 
function provided by Python. Note that you need to check the input is binary number of not.
'''

def is_binary(num):
    for digit in num:
        if digit not in ('0', '1'):
            return False
    return True

def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    
    for digit in reversed(binary_str):
        decimal += int(digit) * (2 ** power)  
        power += 1 
    
    return decimal

binary_str = input("Enter a binary number: ")

if is_binary(binary_str):
    decimal_value = binary_to_decimal(binary_str)
    print(f"Decimal equivalent: {decimal_value}")
else:
    print("Invalid input! Please enter a binary number (only 0s and 1s).")
