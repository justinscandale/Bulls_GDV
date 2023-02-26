import pickle
import csv
import os
import pandas

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

def query_pickle():

    obj = pandas.read_pickle(r'pickled')
    print(obj)

make_pickle()