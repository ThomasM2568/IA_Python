import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

def maxInRow(row):
    return row.max()

df['Row_Max'] = df.apply(maxInRow, axis=1)

print(df)
