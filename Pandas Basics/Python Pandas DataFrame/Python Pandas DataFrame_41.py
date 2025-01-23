import pandas as pd
from datetime import *
date_series = pd.Series(["3/11/2000", "3/12/2000", "3/13/2000"])

datetime_series = pd.to_datetime(date_series)

df = pd.DataFrame()
df['qualify'] = datetime_series

print(df)
