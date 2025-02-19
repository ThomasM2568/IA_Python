# Python Pandas String and Regular Expression

## Code Explanation
<a name="code-explanation"></a>

### Extracting Part of a String (Phone Number)
<a name="extracting-phone-number"></a>
```python
df['company_phone_no'] = df['company_phone_no'].str.split("no. ").str[1]
```
Splits the phone number string and extracts only the phone number by removing the prefix ("no. ").

### Extracting Numeric Values from a String (Year)
<a name="extracting-year"></a>
```python
df['year'] = df['year'].str.extract('(\d+)').astype(int)
```
Extracts the numeric year from the string and converts it to an integer for further operations.

### Filtering Data Based on Year Range
<a name="filtering-by-year-range"></a>
```python
filtered_df = df[(df['year'] >= x) & (df['year'] <= y)]
```
Filters the DataFrame based on a specific range of years, selecting only rows within the defined range.

### Removing HTML Tags from Strings
<a name="removing-html-tags"></a>
```python
df['without_tags'] = df['address'].apply(lambda x: re.sub('<.*?>', '', x))
```
Uses regular expressions to remove HTML tags from the 'address' column, cleaning up the text.

### Capitalizing a String Column
<a name="capitalizing-names"></a>
```python
df['name'] = list(map(lambda x: x.capitalize(), df['name']))
```
Capitalizes the first letter of each word in the 'name' column, ensuring consistent formatting.

## Conclusion
<a name="conclusion"></a>
- **String splitting** and **extraction** techniques allow us to manipulate and clean text data.
- **Filtering** helps select specific rows based on conditions like numeric ranges.
- **Regular expressions** are powerful for cleaning and formatting data, like removing HTML tags.
- **String manipulation functions** such as `.capitalize()` make data consistent and clean for analysis.
