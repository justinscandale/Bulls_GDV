from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/home', methods=["GET","POST"])
def rootPage():
    class_prefix = ''
    class_number = ''
    grade_dist = ''
    if request.method == "POST":
        class_prefix = request.form.get('ClassPrefix')
        class_number = request.form.get('ClassNumber')
        professor_name = request.form.get('ProfessorName')
        grade_dist = calcGradeDist(class_prefix, class_number)
    return render_template("index.html", grade_dist=grade_dist)

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

#flask by deault accepts get methods, must declare if u want more
@app.route('/results', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return 'You have used a post request!'
    else:
        return 'Likely a GET request'
        
app.run()