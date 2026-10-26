# 8) Write a program that finds the common elements between two lists using sets.

list1 = input("Enter the inputs for list 1 :").split(",")
list2 = input("Enter the inputs for list 2 :").split(",")

set1 = set(list1)
set2 = set(list2)

common_element = set1.intersection(set2)

print("common elements between two list : ",common_element)


