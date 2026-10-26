#  What is the output of following code 

# Question 1
xl = {"apple", "Mi", "Vivo"} 
yl = {"google", "microsoft", "apple","Mi"} 
zl = xl.symmetric_difference_update(yl) 
print(zl) 
print(xl)
print(yl)

# Question 2
l= [23,34,54, 12 ,35, 76,87,67, 98, 70]
print(l[-1 : : -3])

# Question 3
str1= ["d",1,"f"]
str2=["d",1,"f"]
str3=str1 
print(str1 is str2)

# Question 4
x = 30/2*((3+2)*(4+2))
print(x)

# Question 5
var1 = "python"*2*1
var = var1.split("y")
print(var)

# Question 6
def add(*no):
    sum=0
    for x in no:
        sum += x
    return sum

print(add(34,65,12,76))
print(add(13))

# Question 7
C = 5 
def This(): 
    C = 1
    for I in (1, 2, 3): 
        C += 1 
This() 
print(C) 

# Question 8
L =["C",10,"S",20,"E",30] 
t = 0 
s = "" 
i = 0 
for c in range(1,6,2): 
    t += c
    s += L[c-1] + "@" 
    i += L[c] 
print(t, i, s) 

# Question 9
def cal (n1, n2=3): 
    result = n1 * n2 
    print( result) 
cal(5, 5) 
cal(6)

# Question 10
a = 20
b = 2
a/=a>>b
print(a)