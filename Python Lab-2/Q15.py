'''
 Let A = [1, 10, 8, 7, 12, 15, 13, 18, 22, 21, 25, 23, 28] be a list. Modify the list A such 
that it contains only odd numbers which are originally in the list. Note that you are not allowed 
to use any new list in the program.
'''
my_list = [1, 10, 8, 7, 12, 15, 13, 18, 22, 21, 25, 23, 28]
my_list = [x for x in my_list if x%2 != 0]
print(my_list)  
