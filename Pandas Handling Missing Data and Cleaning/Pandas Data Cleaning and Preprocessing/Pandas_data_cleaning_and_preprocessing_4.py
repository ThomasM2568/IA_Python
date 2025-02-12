import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Anna', 'John', 'Mike', 'Anna'],
    'Age': [28, 24, 28, 35, 24],
    'City': ['New York', 'Paris', 'New York', 'Berlin', 'Paris']
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


df_cleaned = df.drop_duplicates()


print("\nDataFrame after removing duplicates:")
print(df_cleaned)