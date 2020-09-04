from bs4 import BeautifulSoup  
import pandas as pd
import requests
from urllib.request import urlopen
import urllib

url = 'https://www.op.gg/statistics/champion/'
response = requests.get("https://www.op.gg/statistics/champion/")
soup = BeautifulSoup(response, "html.parser")
soup.find_all("div",'ChampionStatsTable')

