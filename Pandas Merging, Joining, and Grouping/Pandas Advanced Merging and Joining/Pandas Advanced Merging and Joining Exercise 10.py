import pandas as pd

df1 = pd.DataFrame({
    'ID': [101, 102, 103],
    'Name': ['Lucas', 'Emma', 'Noah']
})

df2 = pd.DataFrame({
    'ID': [101, 102, 103],
    'Age': [28, 34, 26]
})

df3 = pd.DataFrame({
    'ID': [101, 102, 103],
    'Salary': [55000, 62000, 71000]
})

merged_df = pd.merge(pd.merge(df1, df2, on='ID'), df3, on='ID')

print(merged_df)