import json
from pprint import pprint
file=json.load(open("scrape4.json","r+"))

lan_list=[]
language={}

dir_list=[]
directors={}

for dic in file:
	dir_list+=dic["Director"]

	lan_list+=dic["language"]

for i in lan_list:
	if i not in language:
		language[i]=1
	else:
		language[i]+=1

# for j in dir_list:
# 	if j not in directors:
# 		directors[j]=1
# 	else:
# 		directors[j]+=1
pprint(language)
print()
print()
print(lan_list)
# pprint(directors)