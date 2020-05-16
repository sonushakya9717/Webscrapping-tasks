import json
from pprint import pprint

scrape=open("scrape2.json","r+")
a=json.load(scrape)
dict_decade={}
for year in a.keys():
	c=year[-1]
	year=int(year)-int(c)
	decade=[]
	for i in a:
		if int(i)==year or int(i)<year+10 and int(i)>year:
			decade+=a[i]
	dict_decade[year]=decade


b=open("scrape3.json","w+")
json.dump(dict_decade,b,indent=4)