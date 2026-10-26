
'''
Q 13) Write a Python program to find the common elements (intersection) between two given lists without using set operations.
Example:
Input: list1 = [1, 3, 4, 6, 7, 9]  
       list2 = [2, 3, 6, 8, 9]  
Output: [3, 6, 9]
'''

list1 = [1, 3, 4, 6, 7, 9]  
list2 = [2, 3, 6, 8, 9]  
list3 = []
for i in list1:
    if(i in list2):
        list3.append(i)
print(list3)

