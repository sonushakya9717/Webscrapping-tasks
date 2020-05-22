import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time


task4=json.load(open("scrape.json","r+"))
full_data=[]
count=1
for i in task4:
	url=i["link"]
	time.sleep(3)
	data=requests.get(url).text
	soup=BeautifulSoup(data,"html.parser")
	more_details={}
	div=soup.find("div",class_="title_wrapper")
	name=div.find("h1").get_text()
	c=name.split()
	name=""
	for k in range(len(c)-1):
		name+=c[k]+" "
	more_details["Name"]=(name.strip())

	subtext=soup.find("div",class_="subtext")
	a_tag=subtext.find_all("a")
	time=subtext.find("time").text
	yes=[]
	for l in range(len(a_tag)-1):
		yes.append(a_tag[l].text)
	more_details["genre"]=yes

	plot_summary=soup.find("div",class_="plot_summary")
	summary=plot_summary.find("div",class_="summary_text").text
	more_details["Bio"]=(summary.strip())

	credit_summary=plot_summary.find("div",class_="credit_summary_item")
	director=credit_summary.find("a").text
	director_data=[]
	director_data.append(director)
	more_details["Director"]=director_data
	
	poster=soup.find("div",class_="poster")
	poster_link=poster.find("img")["src"]
	more_details["poster_image_url"]=poster_link

	articles=soup.find("div",id="titleDetails")
	article=articles.find_all("div",class_="txt-block")
	if article[0].find("h4").text=="Country:":
		country=article[0].find("a").text
		language=article[1].find("a").text
	else:
		country=article[1].find("a").text
		language=article[2].find("a").text

	language_list=[]
	language_list.append(language)
	more_details["language"]=language_list
	more_details["country"]=country
	more_details["Runtime"]=(time.strip())
	full_data.append(more_details)
	print(count)
	count+=1
scrape44=open("scrape4.json","w+")

json.dump(full_data,scrape44,indent=4)

