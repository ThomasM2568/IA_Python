# Pandas Custom Functions Exercises

## Exercise 2: Apply Custom Function to Rows

### Objective
Apply a custom function to each row to find the maximum value in each row.

### Solution
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

def maxInRow(row):
    return row.max()

df['Row_Max'] = df.apply(maxInRow, axis=1)

print(df)
```

### Explanation
- **`df.apply(maxInRow, axis=1)`**: This applies the `maxInRow` function to each row (`axis=1`) of the DataFrame, returning the maximum value in each row.

## Exercise 3: Apply Custom Function to Columns

### Objective
Apply a custom function to each column to find the maximum value in each column and add a new row with these maximum values.

### Solution
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [12, 5, 6],
    'C': [7, 42, 9]
})

def column_max(column):
    return column.max()

means = df.apply(column_max, axis=0)

df.loc['Max'] = means

print(df)
```

### Explanation
- **`df.apply(column_max, axis=0)`**: This applies the `column_max` function to each column (`axis=0`) of the DataFrame, returning the maximum value in each column.
- **`df.loc['Max'] = means`**: This adds a new row labeled 'Max' to the DataFrame with the maximum values of each column.

## Exercise 7: Apply Custom Function to Rows with Multiple Columns

### Objective
Apply a custom function to each row to calculate a new value based on multiple columns.

### Solution
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': [100, 200, 300]
})

def pow_values(row):
    return (row['A'] ** row['B']) - row['C']

df['A_x_B_-C'] = df.apply(pow_values, axis=1)

print(df)
```

### Explanation
- **`df.apply(pow_values, axis=1)`**: This applies the `pow_values` function to each row (`axis=1`) of the DataFrame, calculating a new value based on the columns 'A', 'B', and 'C'.

## Exercise 13: Apply Custom Function to a Date Column

### Objective
Apply a custom function to a date column to extract the day from each date.

### Solution
```python
import pandas as pd

df = pd.DataFrame({
    'Date': ['2025-02-19', '2025-02-18', '2025-02-17']
})

df['Date'] = pd.to_datetime(df['Date'])

def get_day(date):
    return date.day

df['Day'] = df['Date'].apply(get_day)

print(df)
```

### Explanation
- **`pd.to_datetime(df['Date'])`**: This converts the 'Date' column to datetime objects.
- **`df['Date'].apply(get_day)`**: This applies the `get_day` function to each element in the 'Date' column, extracting the day from each date.

These exercises demonstrate various custom functions in Pandas, including applying functions to rows and columns, handling date columns, and performing calculations based on multiple columns.
