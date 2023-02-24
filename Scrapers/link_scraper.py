from bs4 import BeautifulSoup
import requests
import csv

###CHANGE THIS LINK TO CURRENT YEAR/SEMESTER DATA
url = 'https://justinscandale.github.io/eng_22f.html'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

listA = []
linkUSF = 'http://usfweb.usf.edu/dss/infocenter/'
###CHANGE THIS TO CURRENT YEAR FOR FILE NAME
with open('F22_ENG_Links.csv','w') as file:
    writer = csv.writer(file)
    for item in s.findAll("a",{"title":"Faculty"}):
        writer.writerow([linkUSF + item['href']])


###write function to take xcode from each csv file 