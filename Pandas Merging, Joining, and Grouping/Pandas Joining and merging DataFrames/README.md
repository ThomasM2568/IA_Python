# Pandas Joining and Merging DataFrames

## Code Explanation
<a name="code-explanation"></a>

### 1) Merging DataFrames on Multiple Keys
```python
import pandas as pd

# Create two dataframes with common keys
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})

# Merge dataframes on two common columns (key1 and key2)
merged_data_with_key = pd.merge(data1, data2, on=['key1', 'key2'])
print(merged_data_with_key)
```
- **Merging** based on multiple columns ensures that the data is combined where values match in both columns.

---

### 2) Joining DataFrames on One Key
```python
import pandas as pd

# Create two dataframes with a common key
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})

# Merge dataframes on just one common column (key1)
Joined_columns = pd.merge(data1, data2, on='key1')
print(Joined_columns)
```
- **Joining** is done based on a single column, combining relevant columns from both DataFrames.

---

### 3) Joining DataFrames on Their Index
```python
import pandas as pd

# Create two dataframes with different indexes
data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

# Join dataframes on their index (default behavior for join)
Joined_on_index = data1.join(data2)
print(Joined_on_index)
```
- **Joining on index** is useful when rows in DataFrames correspond to matching index labels.

---

### 4) Concatenating DataFrames Along Rows
```python
import pandas as pd

# Create two dataframes with the same column names
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})

# Concatenate dataframes along rows (axis=0)
Merged_DataFrame = pd.concat([data1, data2], axis=0, ignore_index=True)
print(Merged_DataFrame)
```
- **Concatenating** adds rows from both DataFrames together, optionally resetting the index.

---

### 5) Combining DataFrames with Missing Data
```python
import pandas as pd
import numpy as np

# Create two dataframes with missing data
df1 = pd.DataFrame({
    'A': [np.nan, 0.0, np.nan],
    'B': [3, 4, 5]
})

df2 = pd.DataFrame({
    'A': [1, 1, 3],
    'B': [3.0, np.nan, 3.0]
})

# Combine the dataframes, filling missing values from df2 into df1
result = df1.combine_first(df2)

print("Original DataFrames:")
print(df1)
print(df2)
print("\nCombined DataFrame:")
print(result)
```
- **`combine_first()`** is useful for filling missing values in one DataFrame with corresponding values from another.

---

## Conclusion
- **Merging** is used for combining data based on column values.
- **Joining** is most effective when aligning data based on index or columns.
- **Concatenating** stacks dataframes along rows or columns.
- **Combining** allows filling missing values from one DataFrame with another.
