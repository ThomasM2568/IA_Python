'''Sample Output:
Original Series:
0     1
1     3
2     5
3     8
4    10
5    11
6    15
dtype: int64

Difference of differences between consecutive numbers of the said series:
[nan, 2.0, 2.0, 3.0, 2.0, 1.0, 4.0]
[nan, nan, 0.0, 1.0, -1.0, -1.0, 3.0]'''

import pandas as pd

d = pd.Series([1, 3, 5, 8, 10, 11, 15])

print("Difference of differences between consecutive numbers of the said series:")
print(d.diff().tolist())
print(d.diff().diff().tolist())
