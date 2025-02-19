import pandas as pd

df = pd.DataFrame({
    'Date': ['2025-02-19', '2025-02-18', '2025-02-17']
})

df['Date'] = pd.to_datetime(df['Date'])

def get_day(date):
    return date.day

df['Day'] = df['Date'].apply(get_day)

print(df)

