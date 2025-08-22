import requests 
from bs4 import BeautifulSoup


ENDPOINT = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(ENDPOINT)
website_parser = response.text

soup = BeautifulSoup(website_parser,'html.parser')

title = soup.find_all(name = "h3", class_='title')
# for movie in title:
#     all_movie = movie.getText()
all_movies = [movie.getText() for movie in title]
print(all_movies[::-1])
   



