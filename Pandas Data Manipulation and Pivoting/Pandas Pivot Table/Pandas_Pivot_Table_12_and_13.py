import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.min)
print(table)
table2 = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=np.max)
print(table2)
