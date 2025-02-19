import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', 'Orville'],
    'Age': [25, 30, 22, 25],
    'Salary': [50000, 60000, 70000, 50000]
})

print(df.drop_duplicates())
