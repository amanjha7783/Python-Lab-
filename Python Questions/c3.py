from functools import reduce

li = [1,2,3,4,5,6,7]
sum = reduce((lambda x,y : x + y), (li))
# sum=sum(li) # this is the same as the above line
print(sum)