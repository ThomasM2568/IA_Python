import pandas as pd
import numpy as np

date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(date_rng)))

df.set_index('date', inplace=True)

resampled_mean = df.resample('2D').mean()
resampled_sum = df.resample('2D').sum()
resampled_max = df.resample('2D').max()
resampled_min = df.resample('2D').min()

print("Original Data:")
print(df)
print("\nResampled Data (Mean):")
print(resampled_mean)
print("\nResampled Data (Sum):")
print(resampled_sum)
print("\nResampled Data (Max):")
print(resampled_max)
print("\nResampled Data (Min):")
print(resampled_min)