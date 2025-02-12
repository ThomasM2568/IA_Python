import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Anna', 'John', 'Mike', 'Anna'],
    'Age': [25, 30, 25, 40, 30],
    'City': ['New York', 'Paris', 'New York', 'Chicago', 'Paris']
}


df = pd.DataFrame(data)


duplicates = df.duplicated()

print("Duplicate Rows:")
print(duplicates)