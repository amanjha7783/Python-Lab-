'''
9) Create a 5×5 list of random numbers between 1 and 20. Then write a program that
creates a dictionary whose keys are the numbers and whose values are the how many times
the number occurs, then print the three most common numbers. -> dictionary
'''

list1 = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [5,8,14,7,19]
         ]

new_dict = {}
for i in range(5):
    for j in range(5):
        new_dict[list1[i][j]] = new_dict.get(list1[i][j], 0) + 1
print(new_dict)
