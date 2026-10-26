import pandas as pd

print("Pandas version:", pd.__version__)

# pandas series with python list

lst = [10, 20, 30, 40, 50]
print("List:", lst)
print("\n")

ser1 = pd.Series(lst)
print("Series from list:\n", ser1)
print(type(ser1))

empty_ser = pd.Series([])
print("Empty Series:\n", empty_ser)
print(type(empty_ser))
print("\n")

a = pd.Series(['python', 'java', 'c++', 'ruby'], index=[101, 102, 103, 104])
print("Series with custom index:\n", a)
print("\n")

b = pd.Series(['python', 'java', 'c++', 'ruby'], index=[101, 102, 103, 104], name ='programming language')
print("Series with custom index:\n", b)
print("\n")

scalar_ser = pd.Series(100)
print("Series from scalar value:\n", scalar_ser)
print("\n")

scalar_ser2 = pd.Series(100, index=[1, 2, 3, 4, 5])
print("Series from scalar value with custom index:\n", scalar_ser2)

# pandas series with numpy dictionary

import numpy as np
dict_data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
ser2 = pd.Series(dict_data)
print("Series from dictionary:\n", ser2)
print("\n")

print("Accessing element with index 2:", ser2[2])
print("Accessing multiple elements with indices '0' and '3':\n", ser2[0:3])
print("Maximum value in the series:", ser2.max())

print("Minimum value in the series:", ser2.min())
print("Sum of all elements in the series:", ser2.sum())

print("Mean of the series:", ser2.mean())
print("Standard deviation of the series:", ser2.std())

dict_data2 = pd.Series({'p':[1,5,6], 'q':[4,5,8], 'r':[7,8,9], 's':[10,11,12]})
print("Series from dictionary with list values:\n", dict_data2)