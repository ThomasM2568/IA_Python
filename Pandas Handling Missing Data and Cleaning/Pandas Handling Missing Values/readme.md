# Pandas Handling Missing Values

## Code Explanation
<a name="code-explanation"></a>

### Identifying Missing Values
<a name="identifying-missing-values"></a>
```python
missing_values = df.isnull()
```
Checks for missing values (`NaN`) in the entire DataFrame, returning a boolean DataFrame where `True` represents missing values.

### Identifying Columns with Missing Values
<a name="identifying-columns-with-missing-values"></a>
```python
missing_value_columns = df.columns[df.isnull().any()].tolist()
```
Identifies columns that contain at least one missing value, returning a list of those columns.

### Counting Missing Values in Each Column
<a name="counting-missing-values"></a>
```python
missing_values_count = df.isnull().sum()
```
Counts the number of missing values (`NaN`) in each column, providing a summary of missing data.

### Replacing Specific Non-valuable Data with `NaN`
<a name="replacing-with-na"></a>
```python
df.replace(['?', '--'], np.nan, inplace=True)
```
Replaces specific non-valuable data (e.g., `'?'`, `'--'`) with `NaN`, marking them as missing for consistent handling.

### Filling Missing Values with Specific Values
<a name="filling-missing-values"></a>
```python
df.fillna({
    'ord_no': 'Unknown',
    'purch_amt': 0,
    'ord_date': 'Unknown',
    'customer_id': 'Unknown',
    'salesman_id': 'Unknown'
}, inplace=True)
```
Fills missing values (`NaN`) in specific columns with predefined values, ensuring no `NaN` remains.

## Conclusion
<a name="conclusion"></a>
- **Identifying missing values** helps you detect and manage incomplete data.
- **Counting missing values** enables an overview of how much data is missing in each column.
- **Replacing non-valuable data** like placeholders (`'?'`, `'--'`) with `NaN` ensures that such values are treated as missing.
- **Filling missing values** with meaningful data prevents errors during data analysis and prepares the dataset for further processing.
