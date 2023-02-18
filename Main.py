from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home', methods=["GET","POST"])
def rootPage():
    class_prefix = ''
    class_number = ''
    if request.method == "POST":
        class_prefix = request.form.get('ClassPrefix')
        class_number = request.form.get('ClassNumber')
        professor_name = request.form.get('ProfessorName')
        grade_dist = calcGradeDist(class_prefix, class_number)
    return render_template("index.html", )

def calcGradeDist(class_prefix, class_number, professor_name="NONE"):
    if professor_name == 'NONE':
        #get all data from class/course
        pass
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