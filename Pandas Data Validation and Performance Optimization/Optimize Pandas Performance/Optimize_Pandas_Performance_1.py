import pandas as pd 
import numpy as np 
import time  

np.random.seed(0) 
data = np.random.randint(1, 1000, size=(500000, 1)) 
df = pd.DataFrame(data, columns=['Values'])  


start_time = time.time() 
sum_for_loop = 0 
for value in df['Values']: sum_for_loop += value  
time_for_loop = time.time() - start_time


start_time = time.time() 
sum_method = df['Values'].sum() 
time_sum_method = time.time() - start_time 

print(f"Loop: sum = {sum_for_loop}, time = {time_for_loop} seconds")
print(f"Sum: sum = {sum_method}, time = {time_sum_method} seconds")
print(f"Diff: {time_for_loop-time_sum_method} seconds")


