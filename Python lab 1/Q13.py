'''
. WAP to perform the following task: 
Suppose that you are assigned a task to find the maximum element in a given set of positive integers. 
But, you are not given the whole input at a time, and the data comes in the streaming process. Further, 
the data ends with a non-positive element. You are supposed to compute the maximum element that 
you are given until the current position. Also, you are given only two variables to store the information, 
one is to store the current input value, and other is to save the maximum till current input.  
'''
n = [] 

while True:
    x = int(input("Enter the number : "))
    if(x<0):
        break
    n.append(x)
print("List of numbers:", n)
maximum = max(n)
print("Maximum number:", maximum)

