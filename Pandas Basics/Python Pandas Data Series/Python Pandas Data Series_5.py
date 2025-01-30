import pandas as pd

#Sample Series: 
#Original dictionary:
d = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

"""Converted series:
a    100
b    200
c    300
d    400
e    800
dtype: int64 """

series = pd.Series(d)
print(series)