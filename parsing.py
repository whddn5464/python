from bs4 import BeautifulSoup
page = open("C:/Users/kim96/Desktop/program/python/data/03. test_first.html",'r').read()
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

soup.find_all('p')
links =soup.find_all('a')
links