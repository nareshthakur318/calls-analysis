import pandas as pd

#a = pd.read_csv('newphone_data1.csv',encoding = "ISO-8859-1", index_col=0)


#bb=a[a['network'].str.contains("Vodafone") ==True]

#bb=a[a['network'].str.contains("Meteor") ==True]

#bb=a[a['network'].str.contains("Tesco") ==True]

#bb=a[a['network'].str.contains("Three") ==True]

#bb=a[a['network'].str.contains("landline") ==True]
#print(bb)                                        
#bb.to_csv('Vodafone.csv')
#bb.to_csv('Meteor.csv')
#bb.to_csv('Tesco.csv')
#bb.to_csv('Three.csv')
#bb.to_csv('landline.csv')

#print(bb.shape)                                   


#b = pd.read_csv('Vodafone.csv',encoding = "ISO-8859-1", index_col=0)
#b = pd.read_csv('Meteor.csv',encoding = "ISO-8859-1", index_col=0)
#b = pd.read_csv('Tesco.csv',encoding = "ISO-8859-1", index_col=0)
#b = pd.read_csv('Three.csv',encoding = "ISO-8859-1", index_col=0)
b = pd.read_csv('landline.csv',encoding = "ISO-8859-1", index_col=0)
data=b[b['item'].str.contains("call") ==True]
#print(data) 

n=data.groupby('item')['duration'].sum()  # Get the sum of the scores as per post type
print(n)






