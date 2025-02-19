import pandas as pd


data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}


df = pd.DataFrame(data)


all_non_zero = df.groupby('Year')['Display Value'].apply(lambda x: (x != 0).all())
any_non_zero = df.groupby('Year')['Display Value'].apply(lambda x: (x != 0).any())


years_all_non_zero = all_non_zero[all_non_zero].index.tolist()
years_any_non_zero = any_non_zero[any_non_zero].index.tolist()

print("Years with all non-zero values:", years_all_non_zero)
print("Years with any non-zero values:", years_any_non_zero)