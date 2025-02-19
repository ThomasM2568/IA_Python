# Pandas DataFrame Exercises

## Exercise 26: Replace Values in a DataFrame

### Objective
Replace 'yes' and 'no' values in the 'qualify' column with `True` and `False`.

### Solution
```python
import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
      'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
      'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
      'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)

df['qualify'] = df['qualify'].replace('yes', True).replace('no', False)
print(df)
```

### Explanation
- **`df['qualify'].replace('yes', True).replace('no', False)`**: This replaces 'yes' with `True` and 'no' with `False` in the 'qualify' column.

## Exercise 41: Convert Series of Strings to Datetime

### Objective
Convert a series of date strings to datetime objects and create a DataFrame.

### Solution
```python
import pandas as pd
from datetime import *

date_series = pd.Series(["3/11/2000", "3/12/2000", "3/13/2000"])
datetime_series = pd.to_datetime(date_series)

df = pd.DataFrame()
df['qualify'] = datetime_series

print(df)
```

### Explanation
- **`pd.to_datetime(date_series)`**: This converts the series of date strings to datetime objects.

## Exercise 64: Add Prefix and Suffix to Column Names

### Objective
Add a prefix and a suffix to the column names of a DataFrame.

### Solution
```python
import pandas as pd

data = {
    'W': [68, 75, 86, 80, 66],
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

df = pd.DataFrame(data)

df_prefix = df.add_prefix("A_")
print(f"Prefix: \n {df_prefix} \n")

df_suffix = df.add_suffix("_1")
print(f"Suffix: \n {df_suffix}")
```

### Explanation
- **`df.add_prefix("A_")`**: This adds the prefix "A_" to each column name.
- **`df.add_suffix("_1")`**: This adds the suffix "_1" to each column name.

## Exercise 79: Read Data from Clipboard

### Objective
Read data from the clipboard into a DataFrame.

### Solution
```python
import pandas as pd

print(pd.read_clipboard())
```

### Explanation
- **`pd.read_clipboard()`**: This reads the data from the clipboard into a DataFrame.

## Exercise 80: Check for Inequality Between DataFrames

### Objective
Check for inequality between two DataFrames.

### Solution
```python
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
```

### Explanation
- **`df1 != df2`**: This checks for inequality between corresponding elements of `df1` and `df2`.

## Exercise 81: Get Lowest n Records Within Each Group

### Objective
Get the lowest `n` records within each group of a DataFrame.

### Solution
```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
})

print("Original DataFrame")
print(df)

n = 3

result = df.groupby('col1').apply(lambda x: x.nsmallest(n, 'col3')).reset_index(drop=True)

print("\nLowest n records within each group of a DataFrame:")
print(result)
```

### Explanation
- **`df.groupby('col1').apply(lambda x: x.nsmallest(n, 'col3')).reset_index(drop=True)`**: This groups the DataFrame by 'col1', applies a function to get the `n` smallest values in 'col3' within each group, and resets the index.

These exercises demonstrate various DataFrame techniques in Pandas, including replacing values, converting data types, adding prefixes and suffixes, reading data from the clipboard, checking for inequality, and grouping data.
