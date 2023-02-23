import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests 

url = 'https://justinscandale.github.io/index.html'
html = requests.get(url)
s = BeautifulSoup(html.content,"html.parser")
listtemp = []
j = 1
for row in s.find_all('tr'):
    listtemp2 = []
    i = 0
    for row2 in row.find_all('td'):
        if i <22:
            listtemp2.append(row2.get_text())
            i+=1
        else:
            break
    if j> 18 and j < 523:
        listtemp.append(listtemp2)
    j+=1
df = pd.DataFrame(listtemp)
df.to_csv('nmbers.csv',index=False)