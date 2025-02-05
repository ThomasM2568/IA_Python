import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Lucas', 'Emma', 'Noah'],
    'Age': [28, 34, 26]
}, index=[101, 102, 103])

df2 = pd.DataFrame({
    'Salary': [55000, 62000, 71000]
}, index=[101, 102, 103])


joined_df = df1.join(df2)

print(joined_df)