### 1) Checking for Missing Data (NaN values)
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', None],
    'Age': [25, 30, None, 22],
    'Salary': [50000, None, 70000, 60000]
})

print(df.isna().any())
```
- **`isna()`** checks for missing values, and **`any()`** returns True if any value in each column is missing.

---

### 2) Checking Data Types
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', None],
    'Age': [25, '30', 22, 35],
    'Salary': [50000, 60000, '70000', 80000]
})

print(df.dtypes)
```
- **`dtypes`** shows the data type of each column, helpful for data validation.

---

### 3) Dropping Duplicates
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', 'Orville'],
    'Age': [25, 30, 22, 25],
    'Salary': [50000, 60000, 70000, 50000]
})

print(df.drop_duplicates())
```
- **`drop_duplicates()`** removes duplicate rows from the DataFrame.

--- 

These scripts cover basic validation checks like missing data, data types, and duplicates.
