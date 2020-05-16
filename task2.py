import json
from pprint import pprint


scrape=open("scrape.json","r+")

main_dict={}
a=json.load(scrape)
for i in a:
	if str(i["c_year"]) not in main_dict:
		main_dict[i["c_year"]]=[]
		for j in a:
			if i["c_year"]==j["c_year"]:
				main_dict[i["c_year"]].append(j)
b=open("scrape2.json","w+")
json.dump(main_dict,b,indent=4)