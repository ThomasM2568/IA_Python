import numpy as np
import pandas as pd
df = pd.read_excel('E:\SaleData.xlsx')
print(pd.pivot_table(df,index=["Region", "Item"], values="Units", aggfunc=np.sum))
