import pandas as pd
import numpy as np


date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='h')
ts = pd.Series(np.random.randn(len(date_rng)), index=date_rng)


daily_ts = ts.resample('D').mean()

print(daily_ts)