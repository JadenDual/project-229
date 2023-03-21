import pandas as pd

dataset = pd.read_csv('r', 'country_vaccinations.csv')

print('shape of dataset is', dataset.shape)
print('count of columns', len(dataset.columns))
print(dataset.columns)

dataset.loc[:,dataset.isna().any()]