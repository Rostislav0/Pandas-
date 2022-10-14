import pandas as pd

Log_1 = pd.read_csv('log_1.csv', sep=';')
Log_2 = pd.read_csv('log_2.csv', sep=';')
# print(pd.concat((Log_1, Log_2), ignore_index=True))

Log_2_success = pd.read_csv('log_2_success.csv', sep=';')
# # print(pd.concat((Log_2, Log_2_success), axis=1))
# print(pd.concat((Log_2, Log_2_success), axis=1))
# print(pd.concat((Log_2, Log_2_success['SUCCESS']), axis=1))

Log_2_success_unsorted = pd.read_csv('log_2_success_unsorted.csv', sep=';')
print(pd.merge(pd.concat((Log_1, Log_2)), Log_2_success_unsorted, on='ID'))
