import pandas as pd 
import numpy as np
import time 

np.random.seed(0) 
data = {
    'A': np.random.randint(-10, 100, size=100000),
    'B': np.random.randint(-10, 100, size=100000)
}
df = pd.DataFrame(data)

condition = 0

start_time = time.time() 
filtered_rows_loop = []
filtered_rows_loop = [row for index,row in df.iterrows() if row['A']>condition]

filtered_df_loop = pd.DataFrame(filtered_rows_loop)
time_for_loop = time.time() - start_time  

start_time = time.time()  
filtered_df_bool = df[df['A'] > condition]
time_boolean_indexing = time.time() - start_time 


print(f"Loop: time = {time_for_loop} seconds")
print(f"Sum: time = {time_boolean_indexing} seconds")
print(f"Diff: {time_for_loop-time_boolean_indexing} seconds")

