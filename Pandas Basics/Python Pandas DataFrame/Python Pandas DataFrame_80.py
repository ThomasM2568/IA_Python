import pandas as pd
import numpy as np


df1 = pd.DataFrame({
    'W': [68.0, 75.0, 86.0, 80.0, np.nan],
    'X': [78.0, 85.0, np.nan, 80.0, 86.0],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
})


df2 = pd.DataFrame({
    'W': [78.0, 75.0, 86.0, 80.0, np.nan],
    'X': [78, 85, 96, 80, 76],
    'Y': [84, 84, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
})

# Checking for inequality
inequality_df = df1 != df2

print("Original DataFrames:")
print(df1)
print(df2)
print("\nCheck for inequality of the said dataframes:")
print(inequality_df)