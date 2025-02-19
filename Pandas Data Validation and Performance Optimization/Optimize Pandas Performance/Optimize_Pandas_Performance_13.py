import pandas as pd
import numpy as np
import time

num_rows = 1000000
date_range = pd.date_range(start='1/1/2020', periods=num_rows, freq='T')
df = pd.DataFrame({'value': np.random.randn(num_rows)}, index=date_range)

resample_freq = 'H'

start_time = time.time()
resampled_df = df.resample(resample_freq).mean()
end_time = time.time()
resample_time = end_time - start_time

start_time = time.time()
manual_resampled_df = df.groupby(pd.Grouper(freq=resample_freq)).mean()
end_time = time.time()
manual_resample_time = end_time - start_time

print(f"Resample method: {resample_time:.6f} seconds")
print(f"Manual resampling: {manual_resample_time:.6f} seconds")

