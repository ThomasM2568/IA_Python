import pandas as pd

data = {
    'Category': ['D', 'D', 'E', 'E', 'F', 'F'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

def custom_agg(x):
    return x.max() - x.min()

grouped = df.groupby('Category').agg(custom_agg)
print(grouped)
