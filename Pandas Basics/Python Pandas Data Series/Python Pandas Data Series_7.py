import pandas as pd

"""Sample Series: 
    Original Data Series:
0       100
1       200
2    python
3    300.12
4       400
dtype: object
Change the said data type to numeric:
0    100.00
1    200.00
2       NaN
3    300.12
4    400.00
dtype: float64"""

d = pd.Series([100,200,"python",300.12,400])
print(pd.to_numeric(d, errors = 'coerce'))