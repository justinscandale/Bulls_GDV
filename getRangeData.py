import pandas as pd
import pickle

#returns the dataFrame to use in query based on the range
# of term requested by user. if left blank should

def getRange(lowerLimit = ''):
    df = pd.read_pickle(r'pickled') # copies the pickled data
    if lowerLimit == '':
        return df
    termList = ['S21','SU21','F21','S22','SU22','F22']#UPDATE THIS LIST WHEN MORE TERMS ARE ADDED
    index = termList.index(lowerLimit)
    print(index)
    newDF = df.loc[df['Term'].isin(termList[index:])]
    return newDF

print(getRange('F22'))
