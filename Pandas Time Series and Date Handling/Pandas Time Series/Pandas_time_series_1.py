import pandas as pd
from datetime import datetime

# a) Datetime object for Jan 15 2012
datetime_obj = pd.to_datetime('2012-01-15')
print("Datetime object for Jan 15 2012:", datetime_obj)

# b) Specific date and time of 9:20 pm
specific_datetime = pd.to_datetime('2012-01-15 21:20')
print("Specific date and time of 9:20 pm:", specific_datetime)

# c) Local date and time
local_datetime = pd.to_datetime(datetime.now())
print("Local date and time:", local_datetime)

# d) A date without time
date_without_time = pd.to_datetime('2012-01-15').date()
print("A date without time:", date_without_time)

# e) Current date
current_date = pd.to_datetime('today').date()
print("Current date:", current_date)

# f) Time from a datetime
time_from_datetime = pd.to_datetime('2012-01-15 21:20').time()
print("Time from a datetime:", time_from_datetime)

# g) Current local time
current_local_time = pd.to_datetime(datetime.now()).time()
print("Current local time:", current_local_time)