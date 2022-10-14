import pandas as pd

Log_1 = pd.read_csv('log_1.csv', sep=';', index_col='ID')
Log_2 = pd.read_csv('log_2.csv', sep=';', index_col='ID')
Log_2_success_unsorted = pd.read_csv('log_2_success_unsorted.csv', sep=';', index_col='ID')

Log_2_success_unsorted.index.names = ['NEW_ID']

print(pd.merge(pd.concat((Log_1, Log_2)), Log_2_success_unsorted, how='left', left_on='ID', right_index=True))
