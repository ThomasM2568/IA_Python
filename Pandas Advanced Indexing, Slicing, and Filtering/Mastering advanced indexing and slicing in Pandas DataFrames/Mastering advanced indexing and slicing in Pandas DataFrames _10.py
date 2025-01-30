import pandas as pd
df = pd.DataFrame({
    'P': [1, 6, 8, 3, 7],
    'Q': [5, 2, 9, 4, 1]
})

print(df.loc[df['P'] > 3])
