'''
 Write python program to split the given list A into two almost equal halves. Keep the first 
half elements in A and create a new list B to store the second half.
'''
# Given list
a = [1, 2, 3, 4, 5, 6,7,8,9,10]
half_length = len(a)//2
length = len(a)

print(a[:half_length])
print(a[half_length: length])