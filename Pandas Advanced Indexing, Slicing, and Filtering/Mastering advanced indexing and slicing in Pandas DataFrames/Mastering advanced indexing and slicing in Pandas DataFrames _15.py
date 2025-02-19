import pandas as pd
import numpy as np


arrays = [
    ['A', 'A', 'A', 'B', 'B', 'B'],
    ['one', 'two', 'three', 'one', 'two', 'three']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'value': [10, 20, 30, 40, 50, 60]}, index=index)


print("Original DataFrame:")
print(df)


condition = (df.index.get_level_values('first') == 'A') & (df['value'] > 15)
filtered_df = df[condition]


print("\nFiltered DataFrame:")
print(filtered_df)