import pandas as pd
# Creation of the DataFrame
df = pd.DataFrame({
    'W': [68.0, 75.0, 86.0, 80.0, None],
    'X': [78.0, 75.0, None, 80.0, 86.0],
    'Y': [84, 94, 89, 86, 86],
    'Z': [86, 97, 96, 72, 83]
})

# Creation of the Series
s = pd.Series([68.0, 75.0, 86.0, 80.0, None])

result = df.ne(s, axis=0)

print("Original DataFrame:")
print(df)
print("\nOriginal Series:")
print(s)
print("\nCheck for inequality of the said series & dataframe:")
print(result)