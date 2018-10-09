from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time

def flipkart():
 my_url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0&otracker1=AS_Query_TrendingAutoSuggest_1_0&as-pos=1&as-type=TRENDING"

 uClient=uReq(my_url)
 page_html=uClient.read()
 uClient.close()
 page_soup=soup(page_html,"html.parser")

 containers=page_soup.find_all("div",{"class":"_3O0U0u"})
 print(len(containers))
 #print(soup.prettify(containers[0]))
 container=containers[0]
 price=container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
 print(price[0].text)
 rating=container.find_all("div",{"class":"niH0FQ"})
 print(rating[0].text)
 for container in containers:
    product_name=container.div.img['alt']
    print(product_name)
    product_price=container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
    price=product_price[0].text
    print(price)
    product_rating=container.find_all("div",{"class":"niH0FQ"})
    rating=product_rating[0].text
    print(rating)

while(True):
    flipkart()
    time.sleep(30)