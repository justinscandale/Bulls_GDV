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

    filename = 'pickled'
    outfile = open(filename,'wb')

    pickle.dump(df, outfile)
    outfile.close()


def query_pickle():

    obj = pandas.read_pickle(r'pickled')
    print(obj)

query_pickle()