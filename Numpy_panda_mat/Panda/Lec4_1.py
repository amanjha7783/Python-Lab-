# Handling Null Values in Pandas

import pandas as pd

# df = pd.read_csv('Dataset.csv')
df = pd.read_csv('Panda/nullDataset.csv')
print("DataFrame from CSV file:\n", df)
print("\n")


print("null values:\n", df.isnull) #check for null values
print("null values:\n", df.isnull().sum())  #sum of null values in each column
print("null values:\n", df.isnull().sum().sum()) #total null values in the DataFrame

#Dropping Row with null values 
print("shape before dropping the row  ",df.shape)
df2 = df.dropna()
print("shape after dropping the row  ",df2.shape)
print("DataFrame after dropping rows with null values:\n", df2)

#Dropping Row with null values 
print("shape before dropping the column  ",df.shape)
df3 = df.dropna(axis=1)  #by default axis=0, to drop columns use axis=1
print("shape after dropping the column  ",df3.shape)
print("DataFrame after dropping columns with null values:\n", df3)

print(df.dropna(how='all'))  #drop row if all values are null
print(df.dropna(how='any'))  #drop row if any value is null
print(df.dropna(thresh=5))   #drop row if it has less than 5 non-null values

# Filling null values with a specific value
df4 = df.fillna("No Value")
print("DataFrame after filling null values:\n", df4)
# Filling null values with the mean of the column
df5 = df.fillna(df.mean(numeric_only=True))
print("DataFrame after filling null values with mean:\n", df5)

print(df.dropna(inplace=False))  #drop row with null values without modifying the original DataFrame

print(df.dropna(inplace=True))   #drop row with null values and modify the original DataFrame
print("DataFrame after dropping rows with null values (inplace=True):\n", df)