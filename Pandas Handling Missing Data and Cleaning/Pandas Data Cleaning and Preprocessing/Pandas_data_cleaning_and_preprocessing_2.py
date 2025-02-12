import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', None],
    'Age': [28, 22, 35, None, 30],
    'City': ['New York', 'Paris', None, 'Berlin', 'Tokyo']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop rows with missing data
df_cleaned = df.dropna()

# Display cleaned DataFrame
print("\nDataFrame after dropping rows with missing data:")
print(df_cleaned)