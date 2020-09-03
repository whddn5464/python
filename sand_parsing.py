from bs4 import BeautifulSoup 
from urllib.request import urlopen
from urllib.parse import urljoin
import re
import pandas as pd

url_base = 'http://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = url_base + url_sub

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

soup
print(soup.find_all('div','sammy')[0])
len(soup.find_all('div','sammy'))
tmp_one = soup.find_all('div', 'sammy')[0]
type(tmp_one)
tmp_one.find(class_='sammyListing').get_text()
tmp_one.find(class_='sammyListing').get_text()
tmp_one.find('a')['href']
tmp_string = tmp_one.find(class_='sammyListing').get_text()
re.split(('\n|\r\n'), tmp_string)
print(re.split(('\n|\r\n'), tmp_string)[0])
print(re.split(('\n|\r\n'), tmp_string)[1])

rank = []
main_menu = []
cafe_name = []
url_add = []

list_soup = soup.find_all('div', 'sammy')

for item in list_soup:
    rank.append(item.find(class_='sammyRank').get_text())
    
    tmp_string = item.find(class_='sammyListing').get_text()

    main_menu.append(re.split(('\n|\r\n'), tmp_string)[0])
    cafe_name.append(re.split(('\n|\r\n'), tmp_string)[1])
    
    url_add.append(urljoin(url_base, item.find('a')['href']))
cafe_name[:8]
data = {'Rank':rank, 'Menu':main_menu, 'Cafe':cafe_name, 'URL':url_add}
df = pd.DataFrame(data)

df = pd.DataFrame(data, columns=['Rank','Cafe','Menu','URL'])
df.head()
df['URL'][0]
html = urlopen(df['URL'][0])
soup_tmp = BeautifulSoup(html, "html.parser")
# soup_tmp
print(soup_tmp.find('p', 'addy'))
price_tmp = soup_tmp.find('p', 'addy').get_text()
# price_tmp
price_tmp.split()
' '.join(price_tmp.split()[1:-2])
price = []
address = []

for n in df.index[:4]:
    html = urlopen(df['URL'][n])
    soup_tmp = BeautifulSoup(html, "html.parser")
    
    gettings = soup_tmp.find('p', 'addy').get_text()
    
    price.append(gettings.split()[0][:-1])
    address.append(' '.join(gettings.split()[1:-2]))

price
