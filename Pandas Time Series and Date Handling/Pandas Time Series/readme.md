
# Pandas Time Series

## Code Explanation
<a name="code-explanation"></a>

### a) Creating a Datetime Object
```python
import pandas as pd
from datetime import datetime

# Datetime object for Jan 15 2012
datetime_obj = pd.to_datetime('2012-01-15')
print("Datetime object for Jan 15 2012:", datetime_obj)
```
Converts a string to a pandas `datetime` object.

### b) Specific Date and Time
```python
# Specific date and time of 9:20 pm
specific_datetime = pd.to_datetime('2012-01-15 21:20')
print("Specific date and time of 9:20 pm:", specific_datetime)
```
Parses a string representing a date and time into a pandas `datetime` object.

### c) Local Date and Time
```python
# Local date and time
local_datetime = pd.to_datetime(datetime.now())
print("Local date and time:", local_datetime)
```
Converts the current local time into a pandas `datetime` object.

### d) Date without Time
```python
# A date without time
date_without_time = pd.to_datetime('2012-01-15').date()
print("A date without time:", date_without_time)
```
Extracts the date component, leaving out the time.

### e) Current Date
```python
# Current date
current_date = pd.to_datetime('today').date()
print("Current date:", current_date)
```
Retrieves the current date in a `datetime.date` format.

### f) Extracting Time from Datetime
```python
# Time from a datetime
time_from_datetime = pd.to_datetime('2012-01-15 21:20').time()
print("Time from a datetime:", time_from_datetime)
```
Extracts only the time component from a `datetime` object.

### g) Current Local Time
```python
# Current local time
current_local_time = pd.to_datetime(datetime.now()).time()
print("Current local time:", current_local_time)
```
Retrieves the current time from the local datetime.

---

### a) Creating a Specific Date Using Timestamp
```python
# Create a specific date using timestamp
specific_date = pd.Timestamp('2023-10-01')
print("Specific date:", specific_date)
```
Creates a `Timestamp` object for a specific date.

### b) Creating Date and Time Using Timestamp
```python
# Create date and time using timestamp
date_and_time = pd.Timestamp('2023-10-01 12:30:45')
print("Date and time:", date_and_time)
```
Creates a `Timestamp` object for both date and time.

### c) Add Time to Current Date Using Timestamp
```python
# Add a time to the current local date using timestamp
current_date = pd.Timestamp(datetime.now().date())
time_to_add = pd.Timedelta(hours=5, minutes=30)
new_date_time = current_date + time_to_add
print("Current date with added time:", new_date_time)
```
Adds a time delta to a `Timestamp` object.

### d) Current Date and Time Using Timestamp
```python
# Current date and time using timestamp
current_date_time = pd.Timestamp.now()
print("Current date and time:", current_date_time)
```
Retrieves the current date and time in `Timestamp` format.

---

### a) Date from Components
```python
# Date from components
year = 2023
month = 10
day = 5
date_from_components = pd.Timestamp(year, month, day)
print("Date from components:", date_from_components)
```
Creates a date from individual year, month, and day components.

### b) Date from String
```python
# Date from string
date_string = "2023-10-05"
date_from_string = pd.to_datetime(date_string)
print("Date from string:", date_from_string)
```
Converts a string to a `datetime` object.

---

### a) Day Before and After a Specific Date
```python
# Function to print the day after and before a specified date
def print_day_before_after(date_str):
    date = pd.to_datetime(date_str)
    day_before = date - pd.Timedelta(days=1)
    day_after = date + pd.Timedelta(days=1)
    print(f"Day before {date_str}: {day_before.strftime('%Y-%m-%d')}")
    print(f"Day after {date_str}: {day_after.strftime('%Y-%m-%d')}")

print_day_before_after('2023-10-01')
```
Calculates and prints the day before and after a specified date.

### b) Days Between Two Dates
```python
# Function to print the days between two given dates
def print_days_between(start_date_str, end_date_str):
    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str)
    days_between = (end_date - start_date).days
    print(f"Days between {start_date_str} and {end_date_str}: {days_between} days")

print_days_between('2023-10-01', '2023-10-10')
```
Calculates and prints the number of days between two dates.

---

## Conclusion
- **Datetime and Timestamp objects** allow manipulation of time and date efficiently.
- **Time deltas** can be used for adding or subtracting time.
- **String parsing** enables the creation of date and time objects from various formats.
