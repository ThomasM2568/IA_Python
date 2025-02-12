import pandas as pd
import numpy as np

# Sample data
data = {
    'ord_no': ['70001', np.nan, '70002', '70004', np.nan, '70005', '--', '70010', '70003', '70012', np.nan, '70013'],
    'purch_amt': ['150.5', '270.65', '65.26', '110.5', '948.5', '2400.6', '5760', '?', '12.43', '2480.4', '250.45', '3045.6'],
    'ord_date': ['?', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': ['3002', '3001', '3001', '3003', '3002', '3001', '3001', '3004', '--', '3002', '3001', '3001'],
    'salesman_id': ['5002', '5003', '?', '5001', np.nan, '5002', '5001', '?', '5003', '5002', '5003', '--']
}

# Create DataFrame
df = pd.DataFrame(data)

# Replace non-valuable information with NaN
df.replace(['?', '--'], np.nan, inplace=True)

# Fill missing values with a specific value or method
df.fillna({
    'ord_no': 'Unknown',
    'purch_amt': 0,
    'ord_date': 'Unknown',
    'customer_id': 'Unknown',
    'salesman_id': 'Unknown'
}, inplace=True)

print(df)