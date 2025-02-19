import pandas as pd
import numpy as np

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

filtered_df = df.dropna(axis=1, how='any')
print("Filtered DataFrame (all columns with all entries present):")
print(filtered_df)

nan_info = df.isna()
print("\nNaN information (True indicates NaN):")
print(nan_info)

cleaned_df = df.dropna(axis=0, how='any')
print("\nDataFrame after dropping rows with any NaNs:")
print(cleaned_df)