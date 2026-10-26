# Pivot Table in Pandas

import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 75, 28, 78, 32, 80],
    'Humidity': [65, 50, 70, 55, 60, 52]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nPivot Table:")
pivot_table = pd.pivot_table(df, values=['Temperature', 'Humidity'], index=['Date'], columns=['City'], aggfunc='mean')
print(pivot_table)

