# Pandas Grouping and Aggregating

## Code Explanation
<a name="code-explanation"></a>

### 1) Grouping and Aggregating on School Code with Age Statistics
```python
import pandas as pd

# Create student data DataFrame
pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Grouping by school_code and calculating mean, min, and max for age
print('\nMean, min, and max value of age for each value of the school:')
grouped_single = student_data.groupby('school_code').agg({'age': ['mean', 'min', 'max']})
print(grouped_single)
```
- **Grouping and Aggregating** the data by `school_code` provides the mean, minimum, and maximum ages for each school.

---

### 2) Grouping and Splitting the Data by School Code and Class
```python
import pandas as pd

# Create student data DataFrame
pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Group by both school_code and class and split data
print('\nSplit the said data on school_code, class wise:')
result = student_data.groupby(['school_code', 'class'])
for name, group in result:
    print("\nGroup:")
    print(name)
    print(group)
```
- **Grouping by multiple columns** (`school_code` and `class`) and iterating over each group allows you to access and print subsets of the data based on these keys.

---

### 3) Casting Grouped Data into a List
```python
import pandas as pd

# Create student data DataFrame
pd.set_option('display.max_columns', None)

student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Group by school_code and cast the result to a list
print('\nCast grouping as a list:')
result = student_data.groupby(['school_code'])
print(list(result))
```
- **Casting group results as a list** will display the list of groups created by the `groupby()` method. Each entry consists of the key and the corresponding group DataFrame.

---

### 4) Grouping with Aggregated Statistics (more than one column)
```python
import pandas as pd

# Create student data DataFrame
pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Grouping by school_code and performing aggregation on age, height, and weight
print('\nGrouped Data (Multiple Aggregations):')
grouped_multiple = student_data.groupby('school_code').agg({
    'age': ['mean', 'min', 'max'],
    'height': ['mean', 'max'],
    'weight': 'sum'
})
print(grouped_multiple)
```
- **Multiple Aggregations** can be performed on multiple columns. This example computes the mean, min, and max for `age`, the mean and max for `height`, and the sum for `weight`.

---

## Conclusion
- **Grouping** in Pandas allows you to split the data based on one or more columns and perform aggregated statistics on the groups.
- You can use various **aggregation functions** like `mean`, `sum`, `min`, `max`, and even multiple aggregations at once.
- Iterating over groups with `groupby()` enables flexible handling of data subsets.
