# count the number of vowels in string

s = input("Enter the string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels in the string: ", count)

