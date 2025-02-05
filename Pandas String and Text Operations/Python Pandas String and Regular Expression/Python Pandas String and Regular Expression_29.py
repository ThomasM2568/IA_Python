import pandas as pd
import re

pd.set_option('display.max_columns', 10)

df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
})

df['year'] = df['year'].str.extract('(\d+)').astype(int)

x, y = 1800, 2200

filtered_df = df[(df['year'] >= x) & (df['year'] <= y)]

print("Filtered DataFrame:")
print(filtered_df)
