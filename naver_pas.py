from bs4 import BeautifulSoup  
import pandas as pd
from urllib.request import urlopen
import urllib
from tqdm import tqdm_notebook
url_base = "http://movie.naver.com/"
url_syb = "movie/sdb/rank/rmovie.nhn?sel=cur&date=20200903"
asd='https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20200902'
# page = urlopen(url_base+url_syb)
page = urlopen(asd)

soup = BeautifulSoup(page, "html.parser")
len(soup.find_all('div','tit5'))
movie=[]
for a in range(0,49):
    movie.append(soup.find_all('div','tit5')[a].a.string)

print(movie)    
movie_name = [soup.find_all('div', 'tit5')[n].a.string for n in range(0, 49)]
movie_name
date = pd.date_range('2020-5-1', periods=100, freq='D')
date


movie_date = []
movie_name = []
movie_point = []

for today in date:
    html = "http://movie.naver.com/" + \
                                    "movie/sdb/rank/rmovie.nhn?sel=cur&date={date}"
    response = urlopen(html.format(date=
                                   urllib.parse.quote(today.strftime('%Y%m%d'))))
    soup = BeautifulSoup(response, "html.parser")
    
    end = len(soup.find_all('td', 'point'))
    
    movie_date.extend([today for n in range(0, end)])
    movie_name.extend([soup.find_all('div', 'tit5')[n].a.string for n in range(0, end)])
    movie_point.extend([soup.find_all('td', 'point')[n].string for n in range(0, end)])
movie = pd.DataFrame({'date':movie_date, 'name':movie_name, 
                                      'point':movie_point})
movie.head()