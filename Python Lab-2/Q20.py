'''
Let A and B be two lists with no repeated element in the respective list. Write a program
to merge list B with A (means the list A will be expanded) such that the resultant A still contain
no duplicates.
'''

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
# Convert the lists to sets to remove duplicates and then convert back to lists
a_set = set(a)
b_set = set(b)
# Use the union method to merge the two sets and convert back to a list
a = list(a_set.union(b_set))
print(a)  
