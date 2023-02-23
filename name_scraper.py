import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests 


allInfo={'course_num':[],'last_name':[],'first_name':[],'a_num':[],'b_num':[],'c_num':[],'d_num':[],'f_num':[],'i_num':[],'s_num':[],'w_num':[],'o_num':[],'total_num':[]}


### change name to current link file
with open('Links_F22.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for rowLink in reader:
        url = rowLink[0] #correct gets url from csv of links
        page = requests.get(url)
        s = BeautifulSoup(page.content,'html.parser')
        #gets chunk /specific table
        trs = s.find('table',attrs={'class':'gv_report'})
        #gets trs into list
        tempList = []
        for row in trs.findAll('tr'):
            templist2=[]
            for col in row.findAll('td'):
                templist2.append(col.get_text())
            tempList.append(templist2)
        allInfo['last_name'].append(tempList[1][0]) #set all info list with prof name
        allInfo['first_name'].append(tempList[1][1]) #same as above
        allInfo['course_num'].append(url[url.rindex('=')+1:])
        allInfo['a_num'].append(0)
        allInfo['b_num'].append(0)
        allInfo['c_num'].append(0)
        allInfo['d_num'].append(0)
        allInfo['f_num'].append(0)
        allInfo['i_num'].append(0)
        allInfo['s_num'].append(0)
        allInfo['w_num'].append(0)
        allInfo['o_num'].append(0)
        allInfo['total_num'].append(0)
    
#make dataframe into csv file
df = pd.DataFrame(allInfo)
df.to_csv('F22_Data.csv',index=False)
