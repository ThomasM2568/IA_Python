# Pandas Filtering Exercises


## Exercise 24: Find Years with All Non-Zero Values and Any Non-Zero Values

### Objective
Identify which years have all non-zero values and which years have any non-zero values in the `Display Value` column.

### Solution
```python
import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

all_non_zero = df.groupby('Year')['Display Value'].apply(lambda x: (x != 0).all())
any_non_zero = df.groupby('Year')['Display Value'].apply(lambda x: (x != 0).any())

years_all_non_zero = all_non_zero[all_non_zero].index.tolist()
years_any_non_zero = any_non_zero[any_non_zero].index.tolist()

print("Years with all non-zero values:", years_all_non_zero)
print("Years with any non-zero values:", years_any_non_zero)
```

### Explanation

- **`df.groupby('Year')`**: This groups the DataFrame by the 'Year' column, allowing us to perform operations on each group of data corresponding to each year.
- **`apply(lambda x: (x != 0).all())`**: This applies a lambda function to each group, checking if all values in the 'Display Value' column are non-zero.
- **`apply(lambda x: (x != 0).any())`**: This applies a lambda function to each group, checking if any value in the 'Display Value' column is non-zero.
- **`index.tolist()`**: This converts the index of the resulting Series (which contains the years) to a list.

## Exercise 25: Filter Columns with All Entries Present and Drop Rows with Any NaNs

### Objective
Filter all columns where all entries are present, check which rows and columns have NaN values, and drop rows with any NaNs.

### Solution
```python
import pandas as pd
import numpy as np

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

filtered_df = df.dropna(axis=1, how='any')
print("Filtered DataFrame (all columns with all entries present):")
print(filtered_df)

nan_info = df.isna()
print("\nNaN information (True indicates NaN):")
print(nan_info)

cleaned_df = df.dropna(axis=0, how='any')
print("\nDataFrame after dropping rows with any NaNs:")
print(cleaned_df)
```

### Explanation

- **`df.dropna(axis=1, how='any')`**: This drops columns that contain any NaN values. The `axis=1` parameter specifies that we are operating on columns, and `how='any'` means that if any NaN value is found in a column, that column will be dropped.
- **`df.isna()`**: This returns a DataFrame of the same shape as `df`, with boolean values indicating whether each element is NaN (`True`) or not (`False`).
- **`df.dropna(axis=0, how='any')`**: This drops rows that contain any NaN values. The `axis=0` parameter specifies that we are operating on rows, and `how='any'` means that if any NaN value is found in a row, that row will be dropped.

## Exercise 26: Filter Records Starting from the 'Year' Column and Access Every Other Column

### Objective
Filter all records starting from the 'Year' column and access every other column.

### Solution
```python
import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

filtered_df = df.iloc[:, ::2]

print(filtered_df)
```

### Explanation

- **`df.iloc[:, ::2]`**: This uses integer-location based indexing to select all rows (`:`) and every other column (`::2`), starting from the first column.

## Exercise 27: Filter Records Starting from the 2nd Row and Access Every 5th Row

### Objective
Filter all records starting from the 2nd row and access every 5th row.

### Solution
```python
import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

filtered_df = df.iloc[1::5]

print(filtered_df)
```

### Explanation

- **`df.iloc[1::5]`**: This uses integer-location based indexing to select rows starting from the 2nd row (`1`) and then every 5th row (`::5`).

These exercises demonstrate various filtering techniques in Pandas, including filtering based on conditions, handling NaN values, and accessing specific rows and columns.

Similar code found with 1 license type