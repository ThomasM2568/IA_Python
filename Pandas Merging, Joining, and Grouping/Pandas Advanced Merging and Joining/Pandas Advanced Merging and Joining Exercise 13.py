import pandas as pd

df1 = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'Name': ['Lucas', 'Emma', 'Noah', 'Olivia'],
    'City': ['BE', 'PA', 'MO', 'MU']
})

df2 = pd.DataFrame({
    'ID': [102, 103, 104, 105],
    'Name': ['Emma', 'Noah', 'Olivia', 'Ethan'],
    'City': ['PA', 'MO', 'MU', 'BE'],
    'Age': [34, 26, 29, 30]
})

merged_df = pd.merge(df1, df2, on=['ID', 'City'], how='inner')

print(merged_df)
