import pandas as pd

#a = pd.read_csv('newphone_data1.csv')
#b=a[a['item'].str.contains("call") ==True]
#s = b.to_csv('sumofduration.csv')
a = pd.read_csv('sumofduration.csv')
n=a.groupby('date(month)')['duration'].sum()  # Get the sum of the scores as per post type
print(n)