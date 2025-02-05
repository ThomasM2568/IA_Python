import pandas as pd

data = {
    'Category': ['D', 'D', 'E', 'E', 'F', 'F'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

grouped = df.groupby('Category')
filtered = grouped.filter(lambda x: x['Value'].sum() > 50)

print(filtered)
