from flask import Flask, render_template, request
import csv
import query

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
@app.route('/home', methods=["GET","POST"])
def rootPage():
    class_prefix = ''
    class_number = ''
    professor_name = ''
    term = ''
    data = None
    graph = None
    if request.method == "POST":
        class_prefix = request.form.get('ClassPrefix').lower() if request.form.get('ClassPrefix') != None else ''
        class_number = request.form.get('ClassNumber') if request.form.get('ClassNumber') != None else ''
        professor_name = request.form.get('ProfessorName').lower() if request.form.get('ProfessorName') != None else ''
        term = request.form.get('Term') if request.form.get('Term') != None else ''
        data = query.query_pickle(class_prefix,class_number,professor_name,term)
        if data != None and len(data) != 0:
            sum = query.sumGrades(data)
            graph = query.plotGrades(sum,'Graph')
        else:
            graph = 'No Data For This Query; Try Again'
    return render_template("index.html", graph = graph)
'''
def calcGradeDist(class_prefix, class_number, professor_name="NONE"):
    if professor_name == 'NONE':
        #get all data from class/course
        filename = 'phy2053.csv'

        rows = []
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                rows.append(row)

        updated_rows = rows[1:-1]

        professor_dict = {}
        for i in updated_rows:
            if i[1] in professor_dict:
                professor_dict[i[1]].append([i[0], i[2], i[3], i[4]])
            else:
                professor_dict[i[1]] = [[i[0], i[2], i[3], i[4]]]
        
        return professor_dict
    else:
        #get data for certain professor
        
        return round((703* weight) / (height)**2,2)
'''
#flask by default accepts get methods, must declare if u want more
@app.route('/results', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return 'You have used a post request!'
    else:
        return 'Likely a GET request'
        
app.run()