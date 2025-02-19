# Pandas Indexing

## Code Explanation
<a name="code-explanation"></a>

### Default and Custom Indexing
<a name="default-custom-indexing"></a>
```python

# print the DataFrame with its default numerical index.
print("Default Index:")
print(df.head(len(df.get('school_code'))))

# Setting school_code as the Index
print("\nschool_code as new Index:")
print(df.set_index('school_code'))

# Setting t_id as the Index
print("\nt_id as new Index:")
print(df.set_index('t_id'))
```
Sets different columns as index.

### MultiIndex DataFrame
<a name="multiindex-dataframe"></a>
```python
# Create a MultiIndex from the tuples, naming the levels 'sale' and 'city'
sales_tuples = list(zip(sales, cities))  
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

# Create a DataFrame with random data, using the MultiIndex
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index, columns=['A', 'B', 'C', 'D', 'E'])
```
Demonstrates setting a MultiIndex for structured data organization.

### Extracting Data from MultiIndex
<a name="extracting-multiindex"></a>
```python
#Extract all rows for 'sale1'
rows_sale1 = df.loc['sale1']
print(rows_sale1)

# Select all columns for the row labeled 'sale3'
rows_sale3 = df.loc['sale3']
print(rows_sale3)
```
Extracts rows based on MultiIndex hierarchy.

### Sorting MultiIndex
<a name="sorting-multiindex"></a>
```python
#Sorting the DataFrame on full index
print(df.sort_index()) 

#Sorting based on the first index level ('sale')
print(df.sort_index(level='sale'))

#Sorting based on the second index level ('city')
print(df.sort_index(level='city'))
```
Sorts data based on different MultiIndex levels.

### Custom Row Indexing
<a name="custom-row-indexing"></a>
```python

#Assigns a custom row index range.
df.index = range(100, 100 + len(df))
```
Assigns a custom row index range.

### Selecting Data from MultiIndex
<a name="selecting-multiindex"></a>
```python
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
```
Filters rows using MultiIndex selection techniques.

### Time-based Indexing
<a name="time-based-indexing"></a>
```python
import pandas as pd
print("Create a DataFrame, indexing by date and time:")

dt_range = pd.date_range(start ='2020-05-12 07:10:10', freq ='S', periods = 10)
df_dt = pd.DataFrame({"Sale_amt":[100, 110, 117, 150, 112, 99, 129, 135, 140, 150]},
                            index = dt_range)
print(df_dt)
```
Demonstrates indexing by date and time for time-series analysis.

## Conclusion
<a name="conclusion"></a>
- **Custom and hierarchical indexing** optimizes data access.
- **MultiIndexing** structures and organizes hierarchical data.
- **Sorting MultiIndex levels** improves readability and analysis.
- **Date-time indexing** enables time-series data handling.

