import json 
import requests
from bs4 import BeautifulSoup
import os
from pprint import pprint
data =json.load(open("scrape.json"))
count=1
id_list=[]
for k in data:
	list1=[]
	dead_link=k["link"]
	file_name=dead_link[-10:-1]
	id_list.append(file_name)
	if os.path.exists("/home/banner/Desktop/hulk/webscrapping/task12/"+file_name+"_cast"+".json"):
		# print("hai")
		continue
	else:
		scrape00=open("/home/banner/Desktop/hulk/webscrapping/task12/"+file_name+"_cast"+".json","w+")
		link=requests.get(dead_link+"fullcredits?ref_=tt_cl_sm#cast").text
		soup=BeautifulSoup(link,"html.parser")
		table=soup.find("table",class_="cast_list")
		td=table.findAll("td",class_="")
		for i in td:
			dic1={}
			id_name=i.find("a")["href"]
			id_name=id_name[-10:-1]
			cast=i.text
			cast=cast[2:-2]
			dic1["imdb_id"]=id_name
			dic1["name"]=cast
			list1.append(dic1)
		json.dump(list1,scrape00,indent=4)
		print(count)
		count+=1
with open("idl_list.json","w+") as f:
	json.dump(id_list,f)
