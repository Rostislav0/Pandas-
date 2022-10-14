import pandas as pd

df = pd.read_csv('dataset_345422_8 (2).txt', sep=';')


# x = df.loc[df['IP_PROP32'] == 'XL']
# d = x.loc[x['IP_PROP30'] == 'pink']
# print(d['CP_QUANTITY'] * d['CR_PRICE_1_USD'].sum())


df['cost'] = df.CP_QUANTITY * df.CR_PRICE_1_USD
print(df.groupby(['IP_PROP30', 'IP_PROP32']).cost.sum().loc['pink', 'XL'])
