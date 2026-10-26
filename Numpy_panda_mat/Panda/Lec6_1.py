# use replace  to change data in a DataFrame


import pandas as pd

df = pd.read_csv('Panda/Simple_100_Student_Marks.csv')
print("DataFrame from CSV file:\n", df)
print("\n")

# Replacing values in the DataFrame
df2 = df.replace(to_replace=83, value=85)
print("DataFrame after replacing 83 with 85:\n", df2)

df1 = df.replace(19, 20)
print("DataFrame after replacing 19 with 20:\n", df1)

df3 = df.replace(to_replace=['Maths', 'Science'], value=['Mathematics', 'Natural Science'])
print("DataFrame after replacing subject names:\n", df3)

df4 = df.replace(to_replace=[83,79], value="A Grade", inplace=True) # replace multiple marks with 'A Grade'
print("DataFrame after replacing multiple marks with 'A Grade':\n", df4)

df5 = df.replace('[A-Za-z]',0, regex=True) # replace all string values with 0
print("DataFrame after replacing all string values with 0:\n", df5)

df6 = df.replace(to_replace=14 , method='ffill') # forward fill to replace 14
print("DataFrame after forward filling to replace 14:\n", df6)