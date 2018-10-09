 # purpose

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url="https://www.dominos.co.in/menu/veg-pizzas"

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers=page_soup.find_all("div",{"class":"col-md-4 col-xs-12 col-sm-6"})
#print(len(containers))
#print(soup.prettify(containers[0 ]))
container=containers[0]
#print(container.div.img["alt"])
for container in containers:
    product_name=container.div.img['alt']
    print(product_name)
    product_desci=container.p
    print(product_desci.text)
