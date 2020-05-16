import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
page_soup=BeautifulSoup(page,"html.parser")

# td=page_soup.find_all("td",class_="titleColumn").get_text()
main_div=page_soup.find("div",class_="lister")
tbody=main_div.find("tbody",class_="lister-list")
tr=tbody.find_all("tr")

movie_details=[]
movie_position=0
for i in tr:
	movie_name=i.find("td",class_="titleColumn").a.get_text()
	movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
	movie_position+=1
	movie_rating=i.find("td",class_="ratingColumn imdbRating").get_text()
	dead_movie_link=i.find("td",class_="titleColumn").a["href"]
	movie_link="https://www.imdb.com/"+dead_movie_link
	movie_details.append({"a_position":int(movie_position),"b_name":movie_name,"c_year":int(movie_year),"d_rating":float(movie_rating),"link":movie_link})


a=json.dump(movie_details,indent=4)
b=open("scrape.json","w+")
b.write(a)
print(type(a))
