from bs4 import BeautifulSoup

import requests
url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text)


##url = input("Enter a website to extract the URL's from: ")

#r  = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")

#data = r.text

#print(data)

#soup = BeautifulSoup(data,"html.parser")

#print(soup.find_all('a'))

#for link in soup.find_all('td'):
    #print(link.get('rating column'))
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
print(ratings)
movies = soup.select('td.titleColumn')
imdb =[]
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    data = {"movie_title": movie_title}
    imdb.append(data)
for item in imdb:
    print(item['movie_title'])