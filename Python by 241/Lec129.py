set1 = {1,2,3}
l = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,3,4,5,6]
print(set(l))
set1.add(4)
print(set1)
set1.remove(4)
print(set1)
set1.discard(4)
print(set1) # discard() is used when the element is not present in the set give no error

#  in set you can't store any immutable values 
#  like tuple and  dictonaries
# list also 

if 1 in set1:
    print("1 is present in set1")
else:
    print("1 is not present in set1")

for item in set1:
    print(item)

set2 = {8,9,10,2,3,4}

# union_set = set1.union(set2)
union_set = set1 | set2
print(union_set)

# intersection_set = set1.intersection(set2)
intersection_set = set1 & set2
print(intersection_set)
