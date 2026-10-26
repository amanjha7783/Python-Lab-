'''
Consider that A be a list of integers with duplicates. Find the integer in A which appeared 
most number of times in A. 
'''
def most_frequent_number(A):
    # Step 1: Create a dictionary to count occurrences
    counts = {}  
    for num in A:
        if num in counts:
            counts[num] += 1  # Increment count
        else:
            counts[num] = 1  # Initialize count

    # Step 2: Find the number with the maximum count
    max_count = 0
    most_frequent = None  
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent = num

    return most_frequent

A = [1, 3, 5, 4, 7, 8, 4, 5, 2, 3, 4, 9, 6, 4, 3, 4]
print(f"The most frequent number is: {most_frequent_number(A)}")
