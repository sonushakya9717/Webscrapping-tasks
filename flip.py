
import selenium,time,json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint


# from webdriver_manager.chrome import ChromeDriverManager
a="https://www.flipkart.com/"
browser = webdriver.Chrome("/home/banner/Downloads/chromedriver")
browser.get(a)


time.sleep(3)
browser.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("realme mobiles")
time.sleep(2)
page=browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(5)
a=requests.get(browser.current_url).text
b=BeautifulSoup(a,"html.parser")	
name1=b.find_all("div",class_="_3wU53n")
price1=b.find_all("div",class_="_1vC4OE _2rQ-NK")
mobiles={}
count=0
details=b.find_all("ul",class_="vFw0gD")
for i in name1:
	price2=price1[count].get_text()

	for j in details:

		li=j.find_all("li")

	storage=li[0].get_text()
	display=li[1].get_text()
	battery=li[3].get_text()
	camera=li[2].get_text()

	# print(storage)

	if "mobileName" not in mobiles:
		mobiles[i.get_text()]={"price":price2,"storage":storage,"display":display,"battery":battery,"camera":camera}
		mobiles["mobilePrice"]=price2
	count+=1

# pprint(mobiles)

flip_scrape=open("flip_scrape.json","w")
json.dump(mobiles,flip_scrape,indent=4)

browser.quit()


# browser.close()
# driver.get(a)
# page=driver.execute_script('return document.documentElement.outerHTML')
# driver.quit()
# print(page)




