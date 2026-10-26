



name  = "mississippi"
max_count = {}
for char in name:
    if char in max_count:
        max_count[char] += 1
    else:
        max_count[char] = 1
    
print(max_count)

max_char = max(max_count, key=max_count.get)
max_count = max_count[max_char]


print(f'"{max_char}" appears {max_count} times')
