'''
6) Write a Python function that finds the missing number in a list of integers from 1 to N, where one number is missing.

🔹 Example Input: [1, 2, 4, 5, 6] (Missing: 3)
🔹 Output: Missing Number: 3
'''



A = [0,1,2,3,4,5,7,8,9]

print("Input" ,A )
def missing(A):
    for i in range(9):
        if(A[i] != i):
            break
    return i

print("Missing Number : ", missing(A))