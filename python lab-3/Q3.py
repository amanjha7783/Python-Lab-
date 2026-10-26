'''
Let data= [[10, 3], [5, 4], [7, 5], [3, 6], [2, 7], [0, 8], [1, 9]] be a (two-dimensional) list
representing the data of marks of a classs where [x,y] means x number of students scored
mark y. Write a program to find the average mark of the class.
'''

data = [[10, 3], [5, 4], [7, 5], [3, 6], [2, 7], [0, 8], [1, 9]] 

total_marks = 0
for i in range(len(data)):
    total_marks += data[i][0] * data[i][1] 

total_student = 0
for i in range(len(data)):
    total_student += data[i][0]

print("Total student in class = " ,total_student)
print("sum of total marks of the class = ", total_marks)
avg = total_marks/total_student
print("Average marks of the class = ", avg)  


