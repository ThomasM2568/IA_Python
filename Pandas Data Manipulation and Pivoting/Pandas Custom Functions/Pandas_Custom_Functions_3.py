import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [12, 5, 6],
    'C': [7, 42, 9]
})

def column_max(column):
    return column.max()

means = df.apply(column_max, axis=0)

df.loc['Max'] = means

print(df) 

