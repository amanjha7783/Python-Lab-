matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

print(matrix1)
print(matrix2)

for sublist in matrix1:
    for item in sublist:
        print(item )
print('Accessing elements in a 2D list using')
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        print(matrix2[i][j])  # Accessing elements in a 2D list using
