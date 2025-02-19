# Optimize Pandas Performance

## Code Explanation

### Performance of Loop vs. `sum()` Method
```python
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
```
- **Objective**: This code compares the performance of summing a column using a for-loop versus using the `sum()` method in Pandas.
- **Performance**: It calculates the sum of values for each method and measures the time taken. The loop is expected to be slower than the optimized `sum()` method.

### Querying DataFrame with `.query()` vs. Boolean Indexing
```python
condition = 'A < 20 and B > 8'

start_time = time.time()
result_query = df.query(condition)
end_time = time.time()
print(f"Query method: {end_time - start_time:.6f} seconds")

start_time = time.time()
result_boolean_indexing = df[(df['A'] < 20) & (df['B'] < 8)]
end_time = time.time()
print(f"Boolean indexing: {end_time - start_time:.6f} seconds")
```
- **Objective**: Compare the performance of `.query()` and boolean indexing for filtering rows in a DataFrame.
- **Performance**: Measures the time it takes for both methods to filter data based on the given condition.

### Resampling with `.resample()` vs. Manual Grouping with `.groupby()`
```python
resample_freq = 'H'

start_time = time.time()
resampled_df = df.resample(resample_freq).mean()
end_time = time.time()
resample_time = end_time - start_time

start_time = time.time()
manual_resampled_df = df.groupby(pd.Grouper(freq=resample_freq)).mean()
end_time = time.time()
manual_resample_time = end_time - start_time

print(f"Resample method: {resample_time:.6f} seconds")
print(f"Manual resampling: {manual_resample_time:.6f} seconds")
```
- **Objective**: This compares the built-in `.resample()` method with a manual resampling approach using `.groupby()`.
- **Performance**: Measures the time taken by both methods to resample data at the specified frequency and compares their performance.

### Iterating Over Rows with `.iterrows()` vs. Boolean Indexing
```python
start_time = time.time() 
filtered_rows_loop = [row for index, row in df.iterrows() if row['A'] > condition]
filtered_df_loop = pd.DataFrame(filtered_rows_loop)
time_for_loop = time.time() - start_time  

start_time = time.time()  
filtered_df_bool = df[df['A'] > condition]
time_boolean_indexing = time.time() - start_time

print(f"Loop: time = {time_for_loop} seconds")
print(f"Boolean indexing: time = {time_boolean_indexing} seconds")
print(f"Diff: {time_for_loop - time_boolean_indexing} seconds")
```
- **Objective**: Compare the performance of iterating over rows with `.iterrows()` vs using boolean indexing to filter rows.
- **Performance**: It calculates how long it takes for both approaches to filter rows based on a condition.

## Key Takeaways
1. **Optimized Built-in Methods**: Pandas' built-in methods, such as `.sum()`, `.query()`, and `.resample()`, are generally faster and more efficient than manually iterating or using `groupby()` for operations.
2. **Efficient Indexing**: Boolean indexing is much faster than iterating over rows with `.iterrows()`, which should be avoided for performance-sensitive tasks.
3. **Time Comparisons**: By measuring the time taken by different approaches, you can better understand the performance implications of your choices and optimize code accordingly.
