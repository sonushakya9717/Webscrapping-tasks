import json
from pprint import pprint

from task12 import id_list
data =json.load(open("idl_list.json"))
beta=json.load(open("scrape4.json"))
for i in range(len(data)):
	k=data[i]
	l=beta[i]
	ws13=json.load(open("/home/banner/Desktop/hulk/webscrapping/task12/"+k+"_cast"+".json"))
	l["cast"]=ws13
scrape13=open("scrape13.json","a")
json.dump(beta,scrape13,indent=4)
