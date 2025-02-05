import pandas as pd

df1 = pd.DataFrame({
    'ID': [101, 102, 103],
    'Name': ['Lucas', 'Emma', 'Noah']
})

df2 = pd.DataFrame({
    'ID': [100, 103, 102],
    'Age': [28, 34, 26]
})

merged_df = pd.merge(df1, df2, on='ID', how='outer', indicator=True)

print(merged_df)
