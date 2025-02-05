import pandas as pd

year = 2023
month = 10
day = 5
date_from_components = pd.Timestamp(year, month, day)
print("Date from components:", date_from_components)


date_string = "2023-10-05"
date_from_string = pd.to_datetime(date_string)
print("Date from string:", date_from_string)