import csv
from csv import writer
import requests
from bs4 import BeautifulSoup
links=[]

data=requests.get(" https://www.endslaverynow.org/connect?country=3353#filter").text
soup=BeautifulSoup(data,"html.parser")
tables=soup.find("table",id="responsiveTable")
tbody=tables.find("tbody")
tr=tbody.find_all("tr")
new=open("1.csv","w+",newline='')
spamrow=writer(new)
spamrow.writerow(["Name Of Organisation","Contact","Email Id","Address","Active In","Forms of Abolition","Forms of Slavery"])
for i in tr:
	# print(i)
	k=i.find("td").a["href"]
	links.append(k)
for k in links:
	accounts=requests.get("https://www.endslaverynow.org/"+k).text
	details=BeautifulSoup(accounts,"html.parser")

	name=details.find("div",class_="right").h2.text
	div=details.find("div",class_="left")
	ul=div.find_all("ul")

	address_=div.find("ul").text
	address=(address_[21:]).strip()

	active_in=ul[1].li.text

	abolition_=ul[2].text

	slavery_=ul[3].text
	abolition=(abolition_[20:]).strip()
	slavery=(slavery_[18:]).strip()

	if len(ul)>=5:
		perfect_ul=ul[4].find_all("li")
		if len(perfect_ul)>1:
			telephone_no=perfect_ul[0].text
			email_id=perfect_ul[1].text
		else:
			telephone_no="    Not available"
			email_id="       Not available"
	else:
		telephone_no="     Not available"
		email_id="       Not available"
	active=(active_in[11:]).strip()
	telephone=(telephone_no[4:]).strip()
	email=(email_id[7:]).strip()
	spamrow.writerow([name.strip(),telephone,email,address,active,abolition,slavery])
	
