import pandas as pd
import numpy as np

# Create a time series with minute frequency
rng = pd.date_range('2023-01-01', periods=120, freq='T')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

# Downsample the time series to hourly frequency
ts_hourly = ts.resample('H').mean()

print("Original Time Series (Minute Frequency):")
print(ts.head(10))

print("\nDownsampled Time Series (Hourly Frequency):")
print(ts_hourly.head())