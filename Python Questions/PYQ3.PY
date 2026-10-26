sample_string = "google"
count  = 1
def count_number(string):
    for i in range(0, len(sample_string)):
        for j in range(i + 1, len(sample_string)):
            if(sample_string[i] == sample_string[j]):
                count += 1
    return count

for i in range(0, len(sample_string)):
    print(f"{sample_string[i]} appears {count_number("google")} times")


def char_frequency(s):
    freq_dict = {}  # Initialize an empty dictionary

    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1  # Increment count if character exists
        else:
            freq_dict[char] = 1  # Initialize count if character is new

    return freq_dict

# Example Usage
sample_string = "google.com"
result = char_frequency(sample_string)
print(result)
