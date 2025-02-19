import pandas as pd

df = pd.DataFrame({
    'Name': ['Orville', 'Arturo', 'Ruth', None],
    'Age': [25, 30, None, 22],
    'Salary': [50000, None, 70000, 60000]
})

#Check if variables are None, then return if any is None in each list
print(df.isna().any())
