import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4],
    'D': [np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(data)

# Fill missing values with a specified value
df_filled = df.fillna(0)

print("Original DataFrame:")
print(df)
print("\nDataFrame after filling missing values:")
print(df_filled)