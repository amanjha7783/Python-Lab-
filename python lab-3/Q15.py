'''
Create two separate dictionaries. Merge them into a single dictionary. Print the merged
dictionary. Handle cases where both dictionaries have the same key (decide whether to keep
the first or update it with the second dictionary's value).
'''

# Creating two dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

# Merging dictionaries manually
merged_dict = {}

# Adding all key-value pairs from dict1
for key in dict1:
    merged_dict[key] = dict1[key]

# Adding key-value pairs from dict2 (overwriting if the key exists)
for key in dict2:
    merged_dict[key] = dict2[key]  # Overwrites if key is already in merged_dict

# Printing the merged dictionary
print("Merged Dictionary:", merged_dict)

