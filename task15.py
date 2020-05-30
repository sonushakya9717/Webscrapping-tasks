import json
from pprint import  pprint
with open ("scrape13.json") as scrape:
	a=json.load(scrape)
dict1={}
for i in a:
	cast=i["cast"]
	# print(cast)
	for j in cast:
		idies=(j["imdb_id"])
		names=(j["name"])
		if idies not in dict1:
			dict1[idies]={"name":names,"num_movies":1}
		else:
			dict1[idies]["num_movies"]+=1
with open("scrape15.json","w") as k:
	json.dump(dict1,k,indent=4)
k.close()
