import pandas as pd

#a = pd.read_csv('newphone_data1.csv')
#b=a[a['item'].str.contains("call") ==True]
#print(b) 
#c = b.to_csv('longphone.csv')
d = pd.read_csv('longphone.csv')
e = d.loc[:,["duration"]]
#print(e)

f = e.max()
print(f)
print(d.loc[d['duration'] == 10528.0])  

