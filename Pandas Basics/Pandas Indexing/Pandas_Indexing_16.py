import pandas as pd
import numpy as np

sales = ['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4']
cities = ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']

sales_tuples = list(zip(sales, cities))  
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

df = pd.DataFrame(np.random.randn(8, 5), index=sales_index, columns=['A', 'B', 'C', 'D', 'E'])

print(" DataFrame avec un MultiIndex :")
print(df)

print("\n Tri global du DataFrame sur l'index complet :")
print(df.sort_index())

print("\n Tri selon le premier niveau ('sale') :")
print(df.sort_index(level='sale'))

print("\n Tri selon le deuxième niveau ('city') :")
print(df.sort_index(level='city'))

