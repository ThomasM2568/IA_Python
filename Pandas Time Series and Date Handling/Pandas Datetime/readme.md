# Pandas Datetime

## Code Explanation
<a name="code-explanation"></a>

### 1) Current Date using `Timestamp`
```python
import pandas as pd
from datetime import datetime

# Current date using Timestamp
current_date = pd.Timestamp(datetime.now().date())
print("Current date:", current_date)
```
Converts the current date to a `Timestamp` object.

---

### 2) Handling UFO Sightings Data and Date Manipulation
```python
import pandas as pd

# Read the data from CSV file
df = pd.read_csv(r'ufo.csv')

# Convert the 'Date_time' column to string type
df['Date_time'] = df['Date_time'].astype(str)

# Handle '24:00' time issue by replacing with '00:00' and adjust date
mask = df['Date_time'].str.contains(' 24:00', na=False)
df.loc[mask, 'Date_time'] = df.loc[mask, 'Date_time'].str.replace(' 24:00', ' 00:00')
df.loc[mask, 'Date_time'] = pd.to_datetime(df.loc[mask, 'Date_time']) + pd.Timedelta(days=1)

# Convert the 'Date_time' column to datetime format
df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')

# Get the current date
now = pd.to_datetime('today')

# Display the first few rows of the dataframe and the current date
print("Original Dataframe:")
print(df.head())
print("\nCurrent date:")
print(now)
```
- Converts a string column to `datetime` format, handles '24:00' times, and coerces invalid entries to `NaT`.

---

### 3) Calculating Days Between Current Date and Oldest UFO Sighting
```python
import pandas as pd

# Read the data from CSV file
df = pd.read_csv(r'ufo.csv')

# Handle '24:00' time issue
df['Date_time'] = df['Date_time'].astype(str)
mask = df['Date_time'].str.contains(' 24:00', na=False)
df.loc[mask, 'Date_time'] = df.loc[mask, 'Date_time'].str.replace(' 24:00', ' 00:00')
df.loc[mask, 'Date_time'] = pd.to_datetime(df.loc[mask, 'Date_time']) + pd.Timedelta(days=1)

# Convert 'Date_time' column to datetime format
df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')

# Current date
current_date = pd.Timestamp.now()

# Find the oldest sighting date
oldest_date = df['Date_time'].min()

# Calculate the days between the current date and the oldest sighting
days_between = (current_date - oldest_date).days

# Display the results
print(f"Current Date: {current_date}")
print(f"Oldest Date: {oldest_date}")
print(f"Number of days between Current Date and Oldest Date: {days_between}")
```
- Finds the number of days between the current date and the oldest date in the dataset using `Timestamp` objects.

---

### 4) Filtering UFO Sightings in the Last 40 Years
```python
import pandas as pd

# Read the data from CSV file
df = pd.read_csv(r'ufo.csv')

# Handle '24:00' time issue
df['Date_time'] = df['Date_time'].astype(str)
mask = df['Date_time'].str.contains(' 24:00', na=False)
df.loc[mask, 'Date_time'] = df.loc[mask, 'Date_time'].str.replace(' 24:00', ' 00:00')
df.loc[mask, 'Date_time'] = pd.to_datetime(df.loc[mask, 'Date_time']) + pd.Timedelta(days=1)

# Convert 'Date_time' column to datetime format
df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')

# Current date
current_date = pd.Timestamp.now()

# Set the cutoff date for the last 40 years
cutoff_date = current_date - pd.Timedelta(days=365*40)

# Filter sightings that occurred in the last 40 years
recent_sightings = df[df['Date_time'] >= cutoff_date]

# Display the recent sightings
print("Sightings in the last 40 years:")
print(recent_sightings)
```
- Filters UFO sightings that occurred in the last 40 years based on the `Date_time` column.

---

## Conclusion
- **Timestamp and Datetime Objects** are crucial for handling date and time in datasets.
- **Time manipulation** can be done using `pd.Timedelta` and string-based replacements for time adjustments.
- **Filtering** data based on time criteria, such as calculating the difference between two dates or applying a cutoff, is straightforward with Pandas.
