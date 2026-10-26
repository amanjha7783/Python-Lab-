# Q6) Implement basic string compression using counts of repeated characters (e.g., "aaabbc" → "a3b2c1").

def compress_string(s):
    if not s:
        return ""
    
    compressed = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    
    compressed += s[-1] + str(count)
    return compressed

# Example usage
input_str = "aaabbc"
print("Compressed string:", compress_string(input_str))
