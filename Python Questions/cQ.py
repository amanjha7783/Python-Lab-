#  lambda function 
import math
p = [39.2,45.4,67.9,38.3]

o = []
for i in p:
    o.append((i*9)/5 + 32)

print(o)

f = list(map(lambda x : ((x*9)/5 + 32), p ))
print(f)

a = [1,2,3,4]
b = [17,12,11,10]
c = []

print(list(map(lambda x,y: x+y , a,b))) 

A = [ 1,2,3,4,5]
B= [ 10,10,10,10,10]

def sqr(x):
    return x*x

print(list(map(lambda x, y : y , A,B)))
print(list(map(lambda x, y : y%x or y, A,B)))
print(list(map(lambda X: sqr(X), A)))