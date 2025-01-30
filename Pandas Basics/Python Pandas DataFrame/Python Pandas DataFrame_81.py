import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
})

print("Original DataFrame")
print(df)

n = 3

result = df.groupby('col1').apply(lambda x: x.nsmallest(n, 'col3')).reset_index(drop=True)

print("\nLowest n records within each group of a DataFrame:")
print(result)