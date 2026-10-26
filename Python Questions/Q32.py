#  Transpose of matrice 

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j] = a[j][i]

for r in a:
    print(r)