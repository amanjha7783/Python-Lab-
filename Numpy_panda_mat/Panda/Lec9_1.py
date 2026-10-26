#  Appending DataFrames using pandas concat()

import pandas as pd 

df1 = pd.DataFrame({
    'RollNo': [1, 2, 3, 4, 5],
    'Maths': [57, 80, 98, 32, 48],
    'physics': [80, 88, 84, 91, 87]
})

df2 = pd.DataFrame({
    'RollNo': [1, 2, 3, 4, 5],
    'Maths': [85, 90, 78, 92, 88],
    'physics': [75, 35, 64, 91, 67]
})

print("Append df2 to df1 :")

print(pd.concat([df1, df2], ignore_index=True))
print("\nAppend df2 to df1 with sorted columns :")
print(pd.concat([df1, df2], ignore_index=True, sort=True))

df3 = pd.DataFrame({
    'RollNo': [6, 7, 8],
    'Chemistry': [78, 85, 69]
})

print("\nAppend df3 to df1 with different columns :")
print(pd.concat([df1, df3], ignore_index=True, sort=True))