import requests,json,time
from pprint import pprint
from bs4 import BeautifulSoup

page= requests.get("https://paytm.com/shop/search?q=pickles&from=organic&child_site_id=1&site_id=1&category=101471").text

page_soup = BeautifulSoup(page,"html.parser")
# print(page_soup)

main_div = page_soup.find("div",class_="_3RA-")

sec_div = main_div.find_all("div",class_="_1fje")
time.sleep(2)

name_list=[]
links=["https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV108079879340AD2/1561492149508_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASFAZLANI-FOODFAZL8741913490F964/1561511305762_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASEVERIN-RED-CEVER1125901712941BE/1576836919599_3.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHERS-RECIBIGB9858324B4EA1AA/1562238855498_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASJAGS-DELICIOJAGS686587D3DB19DB/1580378013455_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASPATANJALI-AMBIGB985832E78B4443/1567517464921_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASPRIYA-PICKLEBIGB985832199114D5/1562236967416_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV10807987C0F60D2/1561500755182_0..JPG?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASFAZLANI-FOODFAZL8741917C8968BD/1561511382170_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASJAGS-HOMEMADJAGS686587D876EF4/1579511919926_4.jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHERS-RECIBIGB985832219B1DE2/1562238112477_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHERS-RECIBIGB985832219B1DE2/1562238112477_0.jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV1080798D3168377/1561556957375_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASFAZLANI-FOODFAZL874191F7194084/1561561910198_0..jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASJAGS-DELICIOJAGS68658741A38A0F/1579601127273_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHER-S-RECBIGB9858325A7E3ED/1561502522914_0.jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASPRIYA-PICKLEINNO985832DC8E774A/1561492673036_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV1080798ECF1E667/1561492167005_0..jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASFAZLANI-FOODFAZL874191D47522AA/1568630589505_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHER-S-RECBIGB985832696D8141/1562237157908_0.jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASJAGS-DELICIOJAGS686587BB32280A/1580215038898_5.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASPRIYA-PICKLEBIGB985832FA888FA5/1565267549170_1.jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV10807983673C62B/1561492139285_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASFAZLANI-FOODFAZL87419121DE4837/1561511360145_0..jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHER-S-RECBIGB98583215A760F1/1562237138784_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV10807982EAD8C6B/1561492138666_0..jpg?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASMOTHERS-RECIBIGB9858326F2343E3/1562237153706_0.jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV108079866581499/1561500778438_0..JPG?imwidth=282&impolicy=hq","https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV1080798C95CEB14/1561492153673_0..jpg?imwidth=282&impolicy=hq",
"https://assetscdn1.paytm.com/images/catalog/product/F/FA/FASSUPERV-GOLD-SHIV10807987B0E9BC8/1561500752006_0..JPG?imwidth=282&impolicy=hq"]
price_list=[]
discount_list=[]
for i in sec_div:
	row = i.find_all("div",class_="_2i1r")
	time.sleep(2)
	for j in row:
		name= j.find("div",class_="_2apC").get_text()
		name_list.append(name)
		price = j.find("span",class_="_1kMS").get_text()
		price_list.append(price)
		span=j.find("span",class_="qXdv")
		al=span.find_all("span")
		if len(al)>2:
			discount = j.find("span",class_="c-ax").get_text()
			discount_list.append(discount[1:])
		else:
			discount="0%"
			discount_list.append(discount)


students_file=open("k1.html","w")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title>pickles hi pickles</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<table border='2px'>\n")
students_file.write("<tr><td>Pickles Images</td>\n<td>Pickles Name</td>\n<td>Pickles Price</td>\n<td>Discount</td></tr>")
for k in range(len(discount_list)):
	students_file.write("<tr><td><img src="+links[k]+" style='width:100px;height=100px'></img></td>\n<td>"+name_list[k]+"</td>\n<td>"+price_list[k]+"\n<td>"+discount_list[k]+"</td></tr>")
students_file.write("</table>")
students_file.write("</body>")
students_file.write("<html>")
students_file.close()