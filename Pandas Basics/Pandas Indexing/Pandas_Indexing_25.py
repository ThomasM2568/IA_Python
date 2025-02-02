import pandas as pd


data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)


df.index = range(100, 100 + len(df))

print(df)