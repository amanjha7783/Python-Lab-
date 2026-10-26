'''
Q.2. Let A be a list of integers (read the input from the user). Modify the list A such that the
elements are in the increasing order (all elements in A must be in the modified list).
DO NOT USE NEW LIST. No predefined function is allowed to use, except append() and
remove().
'''

A = list(input("Enter the list of integers: ").split(","))
print("Original List:", A)

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print("Sorted List:", A)