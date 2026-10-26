#  list method in python 

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7) # append 7 at the end of the list
print(l)
l.sort() # sort the list in ascending order
print(l)
l.sort(reverse=True) # sort the list in descending order
print(l)
l.reverse() # reverse the list
print(l)
print(l.index(1)) # find the index of the first occurrence of 1
print(l.count(1)) # count the number of occurrences of 1
m = l.copy()
m[0] = 0  # change the first element of m to 0
print(l)   # original list remains unchanged
print(m)   # copied list with first element changed to 0
l.insert(1, 899) # insert 899 at index 1
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m) # extend the list with elements of m
print(l)