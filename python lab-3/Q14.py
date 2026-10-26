'''
Q.14. Write a Python program that takes a dictionary and swaps its keys and values. If there
are duplicate values, ensure only one key is kept in the new dictionary. Print the modified
dictionary.
'''

# Function to swap keys and values in a dictionary
def swap_keys_values(original_dict):
    swapped_dict = {}
    
    for key, value in original_dict.items():
        if value not in swapped_dict:  # Ensures only one key is kept for duplicate values
            swapped_dict[value] = key
    
    return swapped_dict

# Example dictionary
input_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 4}

# Swapping keys and values
output_dict = swap_keys_values(input_dict)

# Printing the modified dictionary
print("Swapped Dictionary:", output_dict)
