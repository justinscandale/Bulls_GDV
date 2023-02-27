#this module is imported into name_num_scraper.py
#do not use it through here

from bs4 import BeautifulSoup
import requests
import csv


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

