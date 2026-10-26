'''
A father has X number of children. One day he brought Y number of chocolates from the market. 
First, he gave one chocolate to every child, and then he realized that he had left with more than X 
chocolates. So, once again, he gave one chocolate to every child. Similarly, he repeated the process 
whenever he had left with more than or equal to X chocolates. Once, he had left with less than X 
chocolates; he stops the process. Write a program to find how many chocolates every child gets and 
how many chocolates are left with the father.
'''
x = int(input("Number of children are :"))
y = int(input("Number of chocolates are :"))
count = 0
while(x<y):
    y = y - x
    count += 1
    
print("Number of chocolates every child gets is : ", count)
print("Number of chocolates are left with the father is : ", y)
