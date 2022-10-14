import pandas as pd

df = pd.read_csv('dataset_file_storage.csv', sep=';')

x = df.groupby(['CompanyID', 'ProjectID'])['FileSize'].sum()
mean = x.mean()
print(x.loc[x > mean].groupby(['CompanyID']).count().count())
