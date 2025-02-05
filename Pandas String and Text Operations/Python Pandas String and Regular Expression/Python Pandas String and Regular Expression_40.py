import pandas as pd
import re

df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', 
                '102 Dunbar <i></i>St.', '17 West Livingston Court']
})

df['without_tags'] = df['address'].apply(lambda x: re.sub('<.*?>', '', x))
print(df)

