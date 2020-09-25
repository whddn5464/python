import requests
import csv
from bs4 import BeautifulSoup 
headers ={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
page=1
url=f"https://www.op.gg/ranking/ladder/page={page}"
res =requests.get(url)
res.raise_for_status() 
soup= BeautifulSoup(res.text,"lxml")
data=soup.find("table", attrs={"class" : "ranking-table"}).find("tbody").find_all("tr")
a=0
filename = "롤순위.csv"
f= open(filename,"w",encoding="utf-8-sig",newline="")
title="순위	소환사	티어	LP	레벨    승수    패배수  판수  	승률".split()


writer = csv.writer(f)
writer.writerow(title)
for datas in data:
    a=a+1
    
    cols = datas.find_all("td")
    dat=[]

    for i in range(5):
        
        dat.append(cols[i].get_text().strip())
        win=cols[5].find("div",{"class":"winratio-graph__text winratio-graph__text--left"})
        lose=cols[5].find("div",{"class":"winratio-graph__text winratio-graph__text--right"})
        rate=cols[5].find("span",{"class":"winratio__text"})
        su=int(lose.get_text())+int(win.get_text())
    
    dat.append(win.get_text())
    dat.append(lose.get_text())
    dat.append(su)
    dat.append(rate.get_text())
    writer.writerow(dat)    
    
    
    

