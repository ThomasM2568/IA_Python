import pandas as pd

data = [1, 3, 7, 1, 9, 3, 5, 1, 9, 0]
series = pd.Series(data)

min_index = series.idxmin()

max_index = series.idxmax()

print("Original Series:")
print(series)
print("Index of the first occurrence of the smallest and largest value of the said series:")
print(min_index)
print(max_index)