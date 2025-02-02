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


filtered_df = df.loc['A']
print("\nRows where 'first' index is 'A':")
print(filtered_df)


filtered_df = df.xs('two', level='second')
print("\nRows where 'second' index is 'two':")
print(filtered_df)


filtered_df = df.loc[('B', 'three')]
print("\nRows where 'first' index is 'B' and 'second' index is 'three':")
print(filtered_df)