import pandas as pd

#a = pd.read_csv('newphone_data1.csv',encoding = "ISO-8859-1", index_col=0)



#b=a[a['item'].str.contains("call") ==True]
#print(bb)                                        
#b.to_csv('totalrecord2.csv')

d = pd.read_csv('totalrecord2.csv')
                                   

c=d.groupby('item')['duration'].sum()  
print(c)