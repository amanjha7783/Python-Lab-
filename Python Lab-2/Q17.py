'''
 Write a program to check duplicate elements in a list. It should print all the elements 
which are unique in the list. Hint: create a new list which contains non-duplicate elements.  
Also, solve this problem without using any new list. 
'''
x = [1,3,5,7,8,4,5,2,3,4,9,6,4,3]

for i in range(len(x)):
    if x.count(x[i]) == 1:
        print(x[i])

