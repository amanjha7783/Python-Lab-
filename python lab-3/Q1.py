'''
Q.1. Let A be a list of integers (read the input from the user). Modify the list A such that the
minimum element in A is at the start of the list. (Other elements can be in any order, but all
other elements from A must present in the modified list)
DO NOT USE NEW LIST. No predefined function is allowed to use, except append() and
remove().
'''
A = list(input("enter the list of integers: ").split(","))
print(A)

minimum = A[0]
for i in range(len(A)):
    if(A[0]>A[i]):
        minimum = A[i]
A.remove(minimum)
A.insert(0,minimum)

print(A)






