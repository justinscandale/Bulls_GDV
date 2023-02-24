from bs4 import BeautifulSoup
import requests
import csv

###CHANGE THIS LINK TO CURRENT YEAR/SEMESTER DATA
def createLinkCSV(urlMainPage, nameTOexport):
    html = requests.get(urlMainPage)
    s = BeautifulSoup(html.content, 'html.parser')
    listA = []
    linkUSF = 'http://usfweb.usf.edu/dss/infocenter/'
    ###CHANGE THIS TO CURRENT YEAR FOR FILE NAME
    with open(nameTOexport,'w') as file:
        writer = csv.writer(file)
        for item in s.findAll("a",{"title":"Faculty"}):
            writer.writerow([linkUSF + item['href']])

