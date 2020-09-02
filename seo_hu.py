import numpy as np
import pandas as pd
import googlemaps
crime_anal_police = pd.read_csv('C:/Users/kim96/Desktop/program/python/data/02. crime_in_Seoul.csv', thousands=',', 
                                encoding='euc-kr')
crime_anal_police.head()
gmaps_key = "AIzaSyAYPRy8GXl7bVGh16bQb-UCAHHw9SFX914" # 자신의 key를 사용합니다.
gmaps = googlemaps.Client(key=gmaps_key)
gmaps.geocode('서울중부경찰서', language='ko')#결제를해야해서 안된다.