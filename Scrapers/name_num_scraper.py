import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests 
import link_scraper

#create dict to store all data in 21 columns
allInfo={'course_name':[],
        'course_num':[],
        'last_name':[],
        'first_name':[],
        'a_num':[],
        'a_per':[],
        'b_num':[],
        'b_per':[],
        'c_num':[],
        'c_per':[],
        'd_num':[],
        'd_per':[],
        'f_num':[],
        'f_per':[],
        'i_num':[],
        'i_per':[],
        's_num':[],
        's_per':[],
        'u_num':[],
        'u_per':[],
        'w_num':[],
        'w_per':[],
        'o_num':[],
        'o_per':[],
        'total_num':[]}

### scrape professor name and course num off of link CSV named 'link_file'
def scrapeLinks(link_file):
    with open(link_file) as file:
        reader = csv.reader(file, delimiter=',')
        for rowLink in reader:
            url = rowLink[0] #correct gets url from csv of links
            page = requests.get(url)
            print('rowLink')
            print('linkLink')
            s = BeautifulSoup(page.content,'html.parser')
            #gets chunk /specific table
            trs = s.find('table',attrs={'class':'gv_report'})
            #gets trs into list
            try:
                tempList = []
                for row in trs.findAll('tr'):
                    templist2=[]
                    for col in row.findAll('td'):
                        templist2.append(col.get_text())
                    tempList.append(templist2)
                allInfo['last_name'].append(tempList[1][0]) #set all info list with prof name
                allInfo['first_name'].append(tempList[1][1]) #same as above
                allInfo['course_num'].append(url[url.rindex('=')+1:])
            except:
                continue

#scrape all grade nums + percents off main HTML page named 'url'
def scrapeMainPage(url):
    html = requests.get(url)
    s = BeautifulSoup(html.content,"html.parser")
    j = 0
    for row in s.find_all('tr'):
        i = 0
        listtemp = []
        for value in row.find_all('td'):
            if i <22:
                listtemp.append(value.get_text())
                i+=1
            else:
                break
            ###EDIT J value to only include ROWS of DATA
        try:
            crn_Propper = allInfo['course_num'][j]
            length = len(listtemp[0])
            if(listtemp[0][length-6:length-1]==crn_Propper and len(listtemp)== 22):
                allInfo['course_name'].append(listtemp[0])
                allInfo['a_num'].append(listtemp[1])
                allInfo['a_per'].append(listtemp[2])
                allInfo['b_num'].append(listtemp[3])
                allInfo['b_per'].append(listtemp[4])
                allInfo['c_num'].append(listtemp[5])
                allInfo['c_per'].append(listtemp[6])
                allInfo['d_num'].append(listtemp[7])
                allInfo['d_per'].append(listtemp[8])
                allInfo['f_num'].append(listtemp[9])
                allInfo['f_per'].append(listtemp[10])
                allInfo['i_num'].append(listtemp[11])
                allInfo['i_per'].append(listtemp[12])
                allInfo['s_num'].append(listtemp[13])
                allInfo['s_per'].append(listtemp[14])
                allInfo['u_num'].append(listtemp[15])
                allInfo['u_per'].append(listtemp[16])
                allInfo['w_num'].append(listtemp[17])
                allInfo['w_per'].append(listtemp[18])
                allInfo['o_num'].append(listtemp[19])
                allInfo['o_per'].append(listtemp[20])
                allInfo['total_num'].append(listtemp[21])
                j+=1
        except:
                continue

#export data in allInfo to csv w/ name 'csv_name'
def exportData(csv_name):
    df = pd.DataFrame({ key:pd.Series(value) for key, value in allInfo.items() })
    df.to_csv(csv_name,index=False)

# EXAMPLE CALL
# #execution occurs here
# link_scraper.createLinkCSV('https://justinscandale.github.io/eng_22f.html','Link_CSVS/F22_ENG_Links.csv')
# scrapeLinks('Link_CSVS/F22_ENG_Links.csv')
# scrapeMainPage('https://justinscandale.github.io/eng_22f.html')
# exportData('F22_ENG.csv')


url = 'https://justinscandale.github.io/SU21.html'
term = 'SU21_2'

link_scraper.createLinkCSV(url,'Link_CSVS/' + term + '_ENG_LINKS.csv')
test_path = '/Users/justinscandale/Desktop/DevJams_23/Link_CSVS/'
# scrapeLinks('../Link_CSVS/' + term + '_ENG_LINKS.csv')
scrapeLinks(test_path + term + '_ENG_LINKS.csv')
scrapeMainPage(url)
test_path2 = '/Users/justinscandale/Desktop/DevJams_23/termData/'
exportData(test_path2 + term + "_ENG.csv")
