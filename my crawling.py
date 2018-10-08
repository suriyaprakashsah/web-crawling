from bs4 import BeautifulSoup
import requests
response = requests.get('https://stackoverflow.com/questions?page=&sort=newest ')
soup = BeautifulSoup(response.text)
ans = soup.find_all("div",{"data-name": "javascript"})
for i in ans:
    print(i.text)
ans1 = soup.find_all("div",{"data-name": "java"})
for i in ans:
    print(i.text)
ans2 = soup.find_all("div",{"data-name": "c#"})
for j in ans2:
    print(j.text)
ans3 = soup.find_all("div",{"data-name": "php"})
for k in ans3:
    print(k.text)
ans4 = soup.find_all("div",{"data-name": "android"})
for l in ans4:
    print(l.text)
ans5 = soup.find_all("div",{"data-name": "python"})
for m in ans5:
    print(m.text)
ans6 = soup.find_all("div",{"data-name": "jquery"})
for n in ans6:
    print(n.text)
ans7 = soup.find_all("div",{"data-name": "html"})
for o in ans7:
    print(o.text)
ans8 = soup.find_all("div",{"data-name": "c++"})
for p in ans8:
    print(p.text)
ans9 = soup.find_all("div",{"data-name": "ios"})
for q in ans9:
    print(q.text)
ans = soup.find_all(class_ = "dno js-hidden")
for r in ans:
      rs = r.text
      x = rs[0:15]
      print(x)