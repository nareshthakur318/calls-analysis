import pandas as pd

#a = pd.read_csv('newphone_data1.csv')
#b=a[a['date(month)'].str.contains("Oct") ==True]
#b=a[a['date(month)'].str.contains("Nov") ==True]
#b=a[a['date(month)'].str.contains("Dec") ==True]
#b=a[a['date(month)'].str.contains("Jan") ==True]
#b=a[a['date(month)'].str.contains("Feb") ==True]
#b=a[a['date(month)'].str.contains("Mar") ==True]
#print(data) 
#s = b.to_csv('Oct.csv')
#c = b.to_csv('Nov.csv')
#s = b.to_csv('Dec.csv')
#s = b.to_csv('Jan.csv')
#s = b.to_csv('Feb.csv')
#s = b.to_csv('Mar.csv')


#a = pd.read_csv('Oct.csv')
#a = pd.read_csv('Nov.csv')
#a = pd.read_csv('Dec.csv')
#a = pd.read_csv('Jan.csv')
#a = pd.read_csv('Feb.csv')
a = pd.read_csv('Mar.csv')
d=a[a['item'].str.contains("call") ==True]
#print(data)

n=d.groupby('item')['date(month)'].count()  # Get the sum of the scores as per post type
print(n)