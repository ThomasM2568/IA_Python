import pandas as pd
import numpy as np


date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')


df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(date_rng)))


df.set_index('date', inplace=True)


df_upsampled = df.resample('H').asfreq()

print(df_upsampled)