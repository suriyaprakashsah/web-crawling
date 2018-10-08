from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq
import re
import csv

my_url = "https://www.yelp.com/search?ns=1&amp;find_desc=KFC&amp;choq=1&amp;find_loc=San+Francisco%2C+CA"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div",{"class":"search-result natural-search-result scrollable-photos-search-result"})
#print(len(containers))
container = containers[0]
#print(soup.prettify(containers[0]))
name = container.find_all("div", {"class":"media-story"})
#print(name[0].text)
name=container.find_all("span",{"class":"indexed-biz-name"})
#print(name[0].text)
rating = container.find_all("span", {"class":"review-count rating-qualifier"})
#print(rating[0].text)
phonenumber=container.find_all("span",{"class":"biz-phone"})
#print(phonenumber[0].text)
descrpition=container.find_all("div",{"class":"snippet-block"})
#print(descrpition[0].text)
category=container.find_all("span",{"class":"category-str-list"})
#print(category[0].text)
filename="nikhil.csv"
f=open(filename,'w')
headers="name,rating,phonenumber,category,description\n"
f.write(headers)
#adress1=container.find_all("span",{"class":"neighborhood-str-list"})
#print(adress1[0].text)
for container in containers:
    name_container = container.find_all("span", {"class": "indexed-biz-name"})
    name=name_container[0].text.strip()
    rating_container = container.find_all("span", {"class": "review-count rating-qualifier"})
    rating=rating_container[0].text.strip()
    phonenumber_container = container.find_all("span", {"class": "biz-phone"})
    phonenumber=phonenumber_container[0].text.strip()
    descrpition_container = container.find_all("div", {"class": "snippet-block"})
    descrpition=descrpition_container[0].text.strip()
    category_container = container.find_all("span", {"class": "category-str-list"})
    category=category_container[0].text.strip()
    #print("name:" + name)
    #print("rating:" + rating)
    if(rating>="50 reviews"):
        print("name:" + name)
        print("rating:" + rating)
        print("phonenumber: " + phonenumber)
        print("descrpition: " + descrpition)
        print("category: " + category)
    '''print("phonenumber: " + phonenumber)
    print("descrpition: " + descrpition)
    print("category: " + category)'''
    f.write(name +"  " + phonenumber.replace("-","|") +"," + rating +"\n")
    #f.write(name + "" + rating +"," + phonenumber.replace("-","|") + "," + descrpition + "," + category +"\n")
f.close()