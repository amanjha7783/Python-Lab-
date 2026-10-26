# Reading CSV(Common separated values) files using Pandas

import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/people-100.csv')
print("DataFrame from CSV file:\n", df)
print("\n")

# Display columns names
print("Columns names:\n", df.columns)
print("\n")
# Display shape of the DataFrame
print("Shape of the DataFrame:", df.shape)
print("\n")
# Display size of the DataFrame
print("Size of the DataFrame:", df.size)
print("\n")

# Display first 5 rows
print("First 5 rows of the DataFrame:\n", df.head())
print("\n")
# Display last 5 rows
print("Last 5 rows of the DataFrame:\n", df.tail())
print("\n")
# Display specific number of rows
print("First 10 rows of the DataFrame:\n", df.head(10))
print("\n")
# Display DataFrame information
print("DataFrame Information:\n")
print(df.info())
print("\n")
# Display DataFrame statistics
print("DataFrame Statistics:\n", df.describe())
print("\n") 
