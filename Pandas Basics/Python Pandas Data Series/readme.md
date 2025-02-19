# Pandas Data Series Exercises

## Exercise 5: Convert Dictionary to Series

### Objective
Convert a dictionary to a Pandas Series.

### Solution
```python
import pandas as pd

# Sample Series: 
# Original dictionary:
d = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

# Converted series:
series = pd.Series(d)
print(series)
```

### Explanation
- **`pd.Series(d)`**: This converts the dictionary `d` to a Pandas Series.

## Exercise 7: Change Data Type to Numeric

### Objective
Change the data type of a series to numeric, coercing errors to NaN.

### Solution
```python
import pandas as pd

d = pd.Series([100, 200, "python", 300.12, 400])
print(pd.to_numeric(d, errors='coerce'))
```

### Explanation
- **`pd.to_numeric(d, errors='coerce')`**: This converts the elements of the series `d` to numeric values, coercing any errors (non-numeric values) to NaN.

## Exercise 18: Calculate Percentiles

### Objective
Calculate the 0th, 25th, 50th, 75th, and 100th percentiles of a series.

### Solution
```python
import numpy as np
import pandas as pd

d = pd.Series([3.000938, 11.370722, 14.612143, 14.118931, 8.247458, 5.526727])

statistics = np.percentile(d, [0, 25, 50, 75, 100])

print(statistics)
```

### Explanation
- **`np.percentile(d, [0, 25, 50, 75, 100])`**: This calculates the specified percentiles of the series `d`.

## Exercise 26: Calculate Difference of Differences

### Objective
Calculate the difference of differences between consecutive numbers of a series.

### Solution
```python
import pandas as pd

d = pd.Series([1, 3, 5, 8, 10, 11, 15])

print("Difference of differences between consecutive numbers of the said series:")
print(d.diff().tolist())
print(d.diff().diff().tolist())
```

### Explanation
- **`d.diff()`**: This calculates the difference between consecutive elements of the series `d`.
- **`d.diff().diff()`**: This calculates the difference of the differences between consecutive elements of the series `d`.

## Exercise 39: Find Index of First Occurrence of Min and Max Values

### Objective
Find the index of the first occurrence of the smallest and largest value of a series.

### Solution
```python
import pandas as pd

data = [1, 3, 7, 1, 9, 3, 5, 1, 9, 0]
series = pd.Series(data)

min_index = series.idxmin()
max_index = series.idxmax()

print("Original Series:")
print(series)
print("Index of the first occurrence of the smallest and largest value of the said series:")
print(min_index)
print(max_index)
```

### Explanation
- **`series.idxmin()`**: This returns the index of the first occurrence of the minimum value in the series `series`.
- **`series.idxmax()`**: This returns the index of the first occurrence of the maximum value in the series `series`.

## Exercise 40: Check for Inequality Between Series and DataFrame

### Objective
Check for inequality between a series and each column of a DataFrame.

### Solution
```python
import pandas as pd

# Creation of the DataFrame
df = pd.DataFrame({
    'W': [68.0, 75.0, 86.0, 80.0, None],
    'X': [78.0, 75.0, None, 80.0, 86.0],
    'Y': [84, 94, 89, 86, 86],
    'Z': [86, 97, 96, 72, 83]
})

# Creation of the Series
s = pd.Series([68.0, 75.0, 86.0, 80.0, None])

result = df.ne(s, axis=0)

print("Original DataFrame:")
print(df)
print("\nOriginal Series:")
print(s)
print("\nCheck for inequality of the said series & dataframe:")
print(result)
```

### Explanation
- **`df.ne(s, axis=0)`**: This checks for inequality between each element of the series `s` and the corresponding element in each column of the DataFrame `df`.

These exercises demonstrate various data series techniques in Pandas, including converting data types, calculating statistics, and performing element-wise operations.
