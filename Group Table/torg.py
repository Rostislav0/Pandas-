import pandas as pd

df = pd.read_csv('torg.csv', sep=';')
# print(df[['IP_PROP30', 'CP_QUANTITY']].groupby(['IP_PROP30']).sum().idxmax())
# print(df[['IP_PROP32', 'CP_QUANTITY']].groupby(['IP_PROP32']).sum().sort_values(by=['CP_QUANTITY', 'IP_PROP32']))