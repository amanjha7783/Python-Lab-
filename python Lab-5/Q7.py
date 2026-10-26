# Q7) Write a Python function to find the length of the longest substring in a given string that does not contain any repeating characters


def longest_unique_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
input_str = "abcabcbb"
print("Length of longest unique substring:", longest_unique_substring(input_str))
