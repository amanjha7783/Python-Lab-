'''
8) Write a Python program to calculate the average value of the numbers in a
given tuple of tuples.
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
'''

tp = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
averages = [sum(i)/len(i) for i in tp]
print(averages)

# Given tuple of tuples
tp1 = ((10, 10, 10, 12), 
       (30, 45, 56, 45), 
       (81, 80, 39, 32), 
       (1, 2, 3, 4))

# Using zip() to transpose the matrix and calculate column-wise averages
avg = [sum(col) / len(col) for col in zip(*tp1)]

print("Average value of the numbers of the said tuple of tuples:")
print(avg)
