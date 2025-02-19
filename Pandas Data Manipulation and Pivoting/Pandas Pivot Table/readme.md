# Pandas Pivot Table Exercises

## Exercise 6: Create a Pivot Table Summing Units by Region and Item

### Objective
Create a pivot table that sums the 'Units' sold, grouped by 'Region' and 'Item'.

### Solution
```python
import numpy as np
import pandas as pd

df = pd.read_excel('E:/SaleData.xlsx')
print(pd.pivot_table(df, index=["Region", "Item"], values="Units", aggfunc=np.sum))
```

### Explanation
- **`pd.pivot_table(df, index=["Region", "Item"], values="Units", aggfunc=np.sum)`**: This creates a pivot table that groups the data by 'Region' and 'Item', and sums the 'Units' for each group.

## Exercise 12 and 13: Create Pivot Tables for Minimum and Maximum Sale Amounts by Item

### Objective
Create pivot tables that show the minimum and maximum 'Sale_amt' for each 'Item'.

### Solution
```python
import pandas as pd
import numpy as np

df = pd.read_excel('SaleData.xlsx')

# Minimum Sale Amount by Item
table_min = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.min)
print(table_min)

# Maximum Sale Amount by Item
table_max = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.max)
print(table_max)
```

### Explanation
- **`pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.min)`**: This creates a pivot table that groups the data by 'Item' and calculates the minimum 'Sale_amt' for each group.
- **`pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.max)`**: This creates a pivot table that groups the data by 'Item' and calculates the maximum 'Sale_amt' for each group.

## Exercise 9: Create a Pivot Table and Query Specific Manager

### Objective
Create a pivot table that shows the 'Sale_amt' grouped by 'Region', 'Manager', and 'SalesMan', and then query the table for a specific manager.

### Solution
```python
import pandas as pd

df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index=["Region", "Manager", "SalesMan"], values="Sale_amt")
print(table.query('Manager == ["Douglas"]'))
```

### Explanation
- **`pd.pivot_table(df, index=["Region", "Manager", "SalesMan"], values="Sale_amt")`**: This creates a pivot table that groups the data by 'Region', 'Manager', and 'SalesMan', and shows the 'Sale_amt' for each group.
- **`table.query('Manager == ["Douglas"]')`**: This queries the pivot table to filter the rows where the 'Manager' is 'Douglas'.

These exercises demonstrate various pivot table techniques in Pandas, including grouping data, calculating aggregate values, and querying pivot tables.
