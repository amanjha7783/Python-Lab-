'''
Q12) Given a list of integers, rearrange the elements so that all negative numbers appear before positive numbers, while maintaining their original order.
Example:
Input: [12, -7, 5, -3, -9, 2, 8]  
Output: [-7, -3, -9, 12, 5, 2, 8]
'''

list1 = [12, -7, 5, -3, -9, 2, 8] 
list2 = []
list3 = []
for i in list1:
    if(i < 0):
        list2.append(i)
    else:
        list3.append(i)

list4 = list2 + list3
print(list4)