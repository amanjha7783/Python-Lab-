'''
Q.7. Write a python program for the following:
Read two string from the user and verify that the second string is a substring of the first one.
Note that use are not allowed to use any predefined functions, except len().
Hit: use slice operator to solve the problem.
'''

def is_substring(first, second):
    len_first = len(first)
    len_second = len(second)
    
    for i in range(len_first - len_second + 1):
        slice = first[i:i + len_second]
        if slice == second:
            return True
    return False

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

if is_substring(first_string, second_string):
    print("The second string is a substring of the first string.")
else:
    print("The second string is NOT a substring of the first string.")

