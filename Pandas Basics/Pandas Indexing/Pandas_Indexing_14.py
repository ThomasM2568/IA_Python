import pandas as pd
import numpy as np

# Step 1: Define the sales and cities
sales = ['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4']
cities = ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']

# Step 2: Combine sales and cities into tuples and create a MultiIndex
sales_tuples = list(zip(sales, cities))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

# Step 3: Create a DataFrame with random values and the MultiIndex
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)

# Step 4: Print the DataFrame
print("DataFrame with MultiIndex:")
print(df)

# Step 5: Extract a single row based on a tuple index (sale2, city2)
print("\nExtract a single row for ('sale2', 'city2'):")
row_sale2_city2 = df.loc[('sale2', 'city2')]
print(row_sale2_city2)

# Step 6: Extract rows where the first index level is 'sale1' and 'sale3'
print("\nExtract all rows for 'sale1':")
rows_sale1 = df.loc['sale1']
print(rows_sale1)

print("\nExtract all rows for 'sale3':")
rows_sale3 = df.loc['sale3']
print(rows_sale3)

# Step 7: Extract a single value by specifying both index tuple and column index
print("\nExtract value for ('sale1', 'city2') in column index 1:")
value_sale1_city2 = df.loc[('sale1', 'city2'), 1]
print(value_sale1_city2)

print("\nExtract value for ('sale4', 'city1') in column index 4:")
value_sale4_city1 = df.loc[('sale4', 'city1'), 4]
print(value_sale4_city1)

