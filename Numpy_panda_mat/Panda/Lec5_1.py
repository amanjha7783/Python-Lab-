
# Filling Null Values in Pandas

import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/nullDataset.csv')
print("DataFrame from CSV file:\n", df)
print("\n")

print("null values:\n", df.isnull) #check for null values
print("null values:\n", df.isnull().sum())  #sum of null values in each column
print("null values:\n", df.isnull().sum().sum()) #total null values in the DataFrame

# Filling null values with a specific value
df4 = df.fillna("No Value")
print("DataFrame after filling null values:\n", df4)
df5 = df.fillna(method='ffill')  #forward fill
print("DataFrame after forward filling null values:\n", df5)
df6 = df.fillna(method='bfill')  #backward fill
print("DataFrame after backward filling null values:\n", df6)

# Filling null values with the mean of the column
df7 = df.fillna(df.mean(numeric_only=True))
print("DataFrame after filling null values with mean:\n", df7)