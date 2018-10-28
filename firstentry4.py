import pandas as pd

data = pd.read_csv('newphone_data1.csv')

c=data.groupby('date(month)').first()         
print(c)

