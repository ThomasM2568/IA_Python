import pandas as pd

df = pd.read_csv(r'ufo.csv')

df['Date_time'] = df['Date_time'].astype(str) 
mask = df['Date_time'].str.contains(' 24:00', na=False)

df.loc[mask, 'Date_time'] = df.loc[mask, 'Date_time'].str.replace(' 24:00', ' 00:00')
df.loc[mask, 'Date_time'] = pd.to_datetime(df.loc[mask, 'Date_time']) + pd.Timedelta(days=1)

df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')  # `errors='coerce'` mettra NaT en cas d'erreur


current_date = pd.Timestamp.now()

oldest_date = df['Date_time'].min()

days_between = (current_date - oldest_date).days

print(f"Current Date: {current_date}")
print(f"Oldest Date: {oldest_date}")
print(f"Number of days between Current Date and Oldest Date: {days_between}")