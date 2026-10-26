# provides a tutorial on two important Pandas functions: groupby() and merge()

import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/Simple_100_Student_Marks.csv')
print("DataFrame from CSV file:\n", df.head())
print("\n")


# Merging with default 'inner' join

df1 = pd.DataFrame({'Roll No.': [1, 2, 3, 4, 5], 'chemistry_marks': [88, 92, 95, 70, 85]})
df1 = pd.DataFrame({'Roll No.': [1, 2, 3, 4, 5], 'Physics_marks': [88, 92, 95, 70, 85]})

print("Merge DataFrame 1:\n", pd.merge(df, df1, on='Roll No.'))  #merging df and df1 on 'Roll No.' column