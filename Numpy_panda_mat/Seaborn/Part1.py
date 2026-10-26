# Seaborn is a python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  


# Load an example dataset
roll_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maths_marks = [78, 85, 62, 90, 88, 76, 95, 89, 84, 91]
sample_df = pd.DataFrame({"Rollno": roll_no, "Marks": maths_marks})
# Display the first few rows of the dataframe
print(sample_df.head())

sns.lineplot(x="Rollno", y="Marks", data=sample_df)
plt.title("Line Plot of Maths Marks")
plt.show()

