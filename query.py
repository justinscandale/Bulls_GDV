import pickle
import csv
import os
import pandas
import plotly.graph_objects as go
from jinja2 import Template, Environment, FileSystemLoader

#makes pickle based on CSV files
def make_pickle():

    x = os.listdir('termData')

    all_df = []

    for i in x:
        pathx = "termData/" + i

        data = pandas.read_csv(pathx)
        data["Term"] = i.split('.')[0].split("_")[0]
        all_df.append(data)

    df = pandas.concat(all_df, axis=0)
    full_names = []
    
    for row in df['course_name']:
        full_names.append(row)
        
    course_num = []
    course_name = []
    course_type = []
    for name in full_names:
        course_type.append(name[8] if name[8]!=' ' else '-')
        course_num.append(name[4:8])
        course_name.append(name[0:3])

    df['prefix']=course_name
    df['num'] = course_num
    df['type'] = course_type
    print(df)

    filename = 'pickled'
    outfile = open(filename,'wb')

    pickle.dump(df, outfile)
    outfile.close()

#returns the dataFrame to use in query based on the range
# of term requested by user. if left blank should
def getRange(lowerLimit = ''):
    df = pandas.read_pickle(r'pickled') # copies the pickled data
    if lowerLimit == '':
        return df
    termList = ['S21','SU21','F21','S22','SU22','F22']#UPDATE THIS LIST WHEN MORE TERMS ARE ADDED
    index = termList.index(lowerLimit)
    newDF = df.loc[df['Term'].isin(termList[index:])]
    return newDF

#queries data based on input from website: EDGE CASE all data = ''!!!
def query_pickle(pre = '', num1 = '', prof = '', term = ''):


    if pre == '' and prof =='':
        return None

    df = getRange(term)

    #make list of rows with prefix = pre from obj
    if(pre != ''):
        df = df.loc[df['prefix'].str.lower() == pre]
        #make list of rows with course_num = cum1 from df
        if(num1 != ''):
            df = df.loc[df['num'] == num1]
    
    if(prof != ''):
        df = df.loc[df['last_name'].str.lower()==prof]

    df = df.sort_values(by=['a_per'], ascending=False)
    return df.values.tolist()
    
def sumGrades(grades):
    a, b, c, d, f = 0, 0, 0, 0, 0
    for row in grades:
        a += row[4]
        b +=  row[6]
        c += row[8]
        d += row[10]
        f += row[12]
    return [a,b,c,d,f]

def plotGrades(grades, gtitle):
    data = [go.Bar(x=['A','B','C','D','F'],y=grades)]
    layout = go.Layout(title = gtitle)
    fig = go.Figure(data=data, layout=layout)
    plot_html = fig.to_html(full_html=False)
    return plot_html

query_pickle('','','')