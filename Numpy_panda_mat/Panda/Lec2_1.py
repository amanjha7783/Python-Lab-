# panda data frame

import pandas as pd
print("Pandas version:", pd.__version__)

df = pd.DataFrame()
print("Empty DataFrame:\n", df)
print("\n")


#DataFrame from list of listsdata

lst = [1,2,3,4,5]
df1 = pd.DataFrame(lst)
print("DataFrame from list of lists:\n", df1)
print("\n")

lst2 = [[1,2,3,4,5], ['a','b','c','d','e'], [10.5,20.5,30.5,40.5,50.5]]
df2 = pd.DataFrame(lst2)
print("DataFrame from list of lists:\n", df2)
print("\n")

# DataFrame from list of dictionaries

a = [{'Name':'Alice', 'Age':25}, {'Name':'Bob', 'Age':30}, {'Name':'Charlie', 'Age':35}]
df3 = pd.DataFrame(a)
print("DataFrame from list of dictionaries:\n", df3)
print("\n")

b = {'Rool No':pd.Series([1,2,3,4,5]),
     'Name':pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Eva']),
     'Age':pd.Series([25,30,35,40,45])
     }
df4 = pd.DataFrame(b)
print("DataFrame from dictionary of series:\n", df4)
print("\n")