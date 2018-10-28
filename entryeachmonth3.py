import pandas as pd

a = pd.read_csv('newphone_data1.csv')

n=a.groupby('date(month)')['index'].count()   
print(n)