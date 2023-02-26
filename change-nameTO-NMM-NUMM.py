import pandas as pd
import pickle

obj = pd.read_pickle(r'pickled')

full_names = []

for row in obj['course_name']:
    full_names.append(row)
    
course_num = []
course_name = []
course_type = []
for name in full_names:
    course_type.append(name[8] if name[8]!=' ' else '-')
    course_num.append(name[4:8])
    course_name.append(name[0:3])

obj['prefix']=course_name
obj['num'] = course_num
obj['type'] = course_type
print(obj)

