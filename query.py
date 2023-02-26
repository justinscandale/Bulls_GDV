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
    df.set_index('course_num')

    for i in df:
        print(i)



    filename = 'pickled'
    outfile = open(filename,'wb')

    pickle.dump(df, outfile)
    outfile.close()


def query_pickle():

    obj = pandas.read_pickle(r'pickled')
    print(obj)

make_pickle()