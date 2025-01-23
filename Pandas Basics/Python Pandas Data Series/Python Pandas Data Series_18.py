import numpy as np
import pandas as pd

d= pd.Series([3.000938, 11.370722, 14.612143, 14.118931, 8.247458, 5.526727])

statistics = np.percentile(d, [0, 25, 50, 75, 100])

print(statistics)