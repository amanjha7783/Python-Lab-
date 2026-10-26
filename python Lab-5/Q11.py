# Q)11 Write a program to rotate a list left or right by n positions.

def rotate_list(lst, n, direction="left"):
    if not lst:
        return []
    
    n = n % len(lst)  # Handle cases where n > len(lst)
    
    if direction == "right":
        return lst[-n:] + lst[:-n]
    else:  # Default is left rotation
        return lst[n:] + lst[:n]

# Example usage
input_list = [1, 2, 3, 4, 5]
n = 2
print("Left rotation:", rotate_list(input_list, n, "left"))
print("Right rotation:", rotate_list(input_list, n, "right"))
