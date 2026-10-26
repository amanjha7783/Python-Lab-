'''
4) Write a program to sort a dictionary by its values in both ascending and descending order
Input: {'apple': 3, 'banana': 1, 'cherry': 2}
Output (Ascending): {'banana': 1, 'cherry': 2, 'apple': 3}
Output (Descending): {'apple': 3, 'cherry': 2, 'banana': 1}
'''

dict1 = {'apple': 3, 'banana': 1, 'cherry': 2}

for key, value in sorted(dict1.items(), key=lambda item: item[1]):
    print(f"{key}: {value}")
for key, value in sorted(dict1.items(), key=lambda item: item[1], reverse=True):
    print(f"{key}: {value}")
                             

