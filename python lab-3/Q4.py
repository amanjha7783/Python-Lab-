'''
Q.4. Let A= [4, 5, 6, 5, 3, 2, 8, 0, 4, 6, 7, 8, 4, 5, 7, 9, 8, 6, 7, 5, 5, 4, 2, 1, 9, 3, 3, 4, 6, 4] be a
list. Create a new two- dimensional list B= [[ , ], [ , ], ...., [ , ]] such that for an element [x, y]
in B, x denote a value of an element in A and y denotes how many times x appeared in list A.
Note that you are not allowed to use extra lists other than A and B. Further, no predefined
functions are allowed except len(), and apppend().
Output: B = [[4, 6], [5, 5], [6, 4], [3, 3], [2, 2], [8, 3], [0, 1], [7, 3], [9, 2], [1, 1]]
'''

def count(element, list):
   count = 0
   for i in list:
      if(i == element):
         count += 1
   return count

A = [4, 5, 6, 5, 3, 2, 8, 0, 4, 6, 7, 8, 4, 5, 7, 9, 8, 6, 7, 5, 5, 4, 2, 1, 9, 3, 3, 4, 6, 4] 
B = [] 
for i in range(len(A)):
   if not any(A[i] in sub for sub in B):
      B.append([A[i], count(A[i],A)])
print(B)


