import pandas as pd
import numpy as np
import time

num_rows = 1000000
df = pd.DataFrame({
    'A': np.random.randint(0, 100, size=num_rows),
    'B': np.random.randn(num_rows),
    'C': np.random.rand(num_rows)
})

condition = 'A < 20 and B > 8'

start_time = time.time()
result_query = df.query(condition)
end_time = time.time()
print(f"Query method: {end_time - start_time:.6f} seconds")

start_time = time.time()
result_boolean_indexing = df[(df['A'] < 20) & (df['B'] < 8)]
end_time = time.time()
print(f"Boolean indexing: {end_time - start_time:.6f} seconds")


