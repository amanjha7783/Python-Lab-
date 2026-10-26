'''
 A= [3,17,9,2,4,8,97,43,39,10,3,17,1,9,2,4,8,97,43,39] be a list of positive integers. Find 
three lists, one contains all prime numbers in A, second one contains composite numbers in A, 
and the third list contains all other numbers in A which are neither prime nor composite. 
'''
x = [3,17,9,2,4,8,97,43,39,10,3,17,1,9,2,4,8,97,43,39]

def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if (n%i == 0):
            return False 
    return True

a=[]
for i in range (len(x)):
    if(prime(i) == True):
        a.append(i)
print("Prime numbers in the list are: ",a)
    
b = []
for i in range (len(x)):
    if(prime(i) == False and i != 1):
        b.append(i)
print("Composite numbers in the list are: ",b)

c = []
for i in range (len(x)):
    if(i == 1):
        c.append(i)

print("Neither prime nor composite numbers in the list are: ",c)
