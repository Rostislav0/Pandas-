import pandas as pd

orders = pd.read_csv('orders.csv', sep=';')
products = pd.read_csv('Products.csv', sep=';')

products = products.loc[products['Name'].str.contains('Носки')]


x = pd.merge(orders, products, how='inner', left_on='ID товара', right_on='Product_ID')

x = x.loc[x['Оплачен'] == 'Да']
print((x['Количество'] * x['Price']).sum())
