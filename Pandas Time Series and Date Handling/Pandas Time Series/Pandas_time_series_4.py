import pandas as pd

# Function to print the day after and before a specified date
def print_day_before_after(date_str):
    date = pd.to_datetime(date_str)
    day_before = date - pd.Timedelta(days=1)
    day_after = date + pd.Timedelta(days=1)
    print(f"Day before {date_str}: {day_before.strftime('%Y-%m-%d')}")
    print(f"Day after {date_str}: {day_after.strftime('%Y-%m-%d')}")

# Function to print the days between two given dates
def print_days_between(start_date_str, end_date_str):
    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str)
    days_between = (end_date - start_date).days
    print(f"Days between {start_date_str} and {end_date_str}: {days_between} days")

# Example usage
print_day_before_after('2023-10-01')
print_days_between('2023-10-01', '2023-10-10')