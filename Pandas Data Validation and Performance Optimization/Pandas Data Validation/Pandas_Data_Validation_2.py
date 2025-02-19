import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', None],
    'Age': [25, '30', 22, 35],
    'Salary': [50000, 60000, '70000', 80000]
})

print(df.dtypes)

