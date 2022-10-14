import pandas as pd
import numpy as np

my_stat = pd.read_csv('my_stat.csv')

my_stat['V5'] = my_stat['V1'] + my_stat['V4']
my_stat['V6'] = np.log(my_stat['V2'])
my_stat = my_stat.rename({'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'}, axis=1)
# print(my_stat.head())
my_stat_1 = pd.read_csv('my_stat_1.csv')

my_stat_1['session_value'] = my_stat_1['session_value'].fillna(0)

my_stat_1.loc[my_stat_1['n_users'] < 0, 'n_users'] = my_stat_1.query('n_users >= 0')['n_users'].median()
# print(my_stat_1)

mean_session_value_data = my_stat_1.groupby("group", as_index=False).session_value.agg({'mean_session_value': 'mean'})
print(mean_session_value_data)
