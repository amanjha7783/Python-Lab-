# provides a tutorial on two important Pandas functions: groupby() and merge()

import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/Simple_100_Student_Marks.csv')
print("DataFrame from CSV file:\n", df.head())
print("\n")

# Using groupby() to group data based on a column

branch_group = df.groupby(by = 'student_name')  #grouping by 'section' column
print("Group object:\n", branch_group.groups)
print("\n")


branch_group = df.groupby(by = ['student_name', 'social_studies_marks'])  #grouping by 'section' column
print("Group object:\n", branch_group.groups)

