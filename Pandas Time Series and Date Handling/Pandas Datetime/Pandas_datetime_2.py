import pandas as pd

df = pd.read_csv(r'ufo.csv')

df['Date_time'] = df['Date_time'].astype(str) 
mask = df['Date_time'].str.contains(' 24:00', na=False)

df.loc[mask, 'Date_time'] = df.loc[mask, 'Date_time'].str.replace(' 24:00', ' 00:00')
df.loc[mask, 'Date_time'] = pd.to_datetime(df.loc[mask, 'Date_time']) + pd.Timedelta(days=1)

df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')  # `errors='coerce'` mettra NaT en cas d'erreur


now = pd.to_datetime('today')

print("Original Dataframe:")
print(df.head())
print("\nCurrent date:")
print(now)
