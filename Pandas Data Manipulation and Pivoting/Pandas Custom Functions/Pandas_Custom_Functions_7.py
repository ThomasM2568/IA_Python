import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': [100, 200, 300]
})

def pow_values(row):
    return (row['A'] ** row['B'])-row['C']

df['A_x_B_-C'] = df.apply(pow_values, axis=1)

print(df)

