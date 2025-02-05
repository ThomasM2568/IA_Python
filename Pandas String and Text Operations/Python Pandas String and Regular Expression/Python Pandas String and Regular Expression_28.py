import pandas as pd
import re

pd.set_option('display.max_columns', 10)

df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'company_phone_no': ['Company1-Phone no. 4695168357','Company2-Phone no. 8088729013','Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371']
    })

df['company_phone_no'] = df['company_phone_no'].str.split("no. ").str[1]
print(df['company_phone_no'])

