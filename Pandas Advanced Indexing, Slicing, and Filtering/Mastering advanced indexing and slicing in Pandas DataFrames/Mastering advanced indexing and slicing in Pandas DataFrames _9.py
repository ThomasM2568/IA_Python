import pandas as pd

df = pd.DataFrame({
    'X': [1, 6, 8, 3, 7],
    'Y': [5, 2, 9, 4, 1]
})

print(df.iloc[:4])


