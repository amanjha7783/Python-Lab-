
import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/Simple_100_Student_Marks.csv')
print("DataFrame from CSV file:\n", df)
print("\n")

# Locating data using loc 
df1 = df.loc[2]  #locating row with index 2
print("Row with index 2:\n", df1)

df2 = df.loc[0:4]  #locating rows from index 0 to 4
print("Rows from index 0 to 4:\n", df2)

print("social_studies_marks of 5th student:\n", df.loc[4, 'social_studies_marks']) #locating specific cell value

print("science_marks of students from index 2 to 6:\n", df.loc[2:6, 'science_marks']) #locating specific column for multiple rows

print("Students with science marks less than 60:\n", df.loc[df["science_marks"]<60]) #locating rows based on condition

print("Students with maths marks greater than or equal to 70:\n", df.loc[df["maths_marks"]>=70, ["science_marks"]]) #locating rows based on condition
print("\n")

# iloc that uses index positions to locate data
df3 = df.iloc[3]  #locating row at index position 3
print("Row at index position 3:\n", df3)
print("\n")

print("locating multiple rows at index positions 1,2,3 ", df.loc[[1,2,3]])  #locating multiple rows at index positions 1,2,3
print("\n")

print("All the section in 3rd column:\n", df.iloc[:,2])  #locating all the rows in 2nd column
print("\n")


print("first 5 sections in 3rd column:\n", df.iloc[:5,2])  #locating all the rows in 2nd column
print("\n")

print("Rows from index positions 2 to 6 and columns from index positions 1 to 3:\n", df.iloc[2:7,1:4])  #locating rows from index positions 2 to 6 and columns from index positions 1 to 3