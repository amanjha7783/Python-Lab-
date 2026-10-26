''' 
Write a Python program for the following:
 Take at most n integers as input from the user. You do not accept further intputs from the user 
if the sum of the elements entered till now is negative. Finally, display that how many integers 
are given by the user and their sum. (Take the value of n as an input from the user.)
'''
count = 0
sum = 0
while True:
    n = int(input("Enter the number of integers you want to enter: "))
    count += 1
    if(n<0):
        break
    sum = sum + n 
print(count)
print(sum)   