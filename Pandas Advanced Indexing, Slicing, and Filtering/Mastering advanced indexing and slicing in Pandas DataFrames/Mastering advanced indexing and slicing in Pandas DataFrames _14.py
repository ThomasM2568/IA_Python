import pandas as pd
import numpy as np


arrays = [
    ['A', 'A', 'A', 'B', 'B', 'B'],
    ['one', 'two', 'three', 'one', 'two', 'three']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame(np.random.randn(6, 2), index=index, columns=['value1', 'value2'])

print("Original DataFrame:")
print(df)


sliced_df = df.loc['A']

print("\nSliced DataFrame with .loc['A']:")
print(sliced_df)