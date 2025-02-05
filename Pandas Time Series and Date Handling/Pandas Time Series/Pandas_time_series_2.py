import pandas as pd
from datetime import datetime

# a) Create a specific date using timestamp
specific_date = pd.Timestamp('2023-10-01')
print("Specific date:", specific_date)

# b) Create date and time using timestamp
date_and_time = pd.Timestamp('2023-10-01 12:30:45')
print("Date and time:", date_and_time)

# c) Add a time to the current local date using timestamp
current_date = pd.Timestamp(datetime.now().date())
time_to_add = pd.Timedelta(hours=5, minutes=30)
new_date_time = current_date + time_to_add
print("Current date with added time:", new_date_time)

# d) Current date and time using timestamp
current_date_time = pd.Timestamp.now()
print("Current date and time:", current_date_time)