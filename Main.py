from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home', methods=["GET","POST"])
def rootPage():
    class_prefix = ''
    class_number = ''
    weight = ''
    bmi = ''
    if request.method == "POST" and 'weight' in request.form:
        class_prefix = float(request.form.get('height'))
        class_number = float(request.form.get('weight'))
        grade_dist = calcGradeDist(class_prefix, class_number)
    return render_template("index.html", height=height, weight=weight, bmi=bmi)

def calcGradeDist(class_prefix, class_number):
    professors = 
    return round((703* weight) / (height)**2,2)

#flask by deault accepts get methods, must declare if u want more
@app.route('/results', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return 'You have used a post request!'
    else:
        return 'Likely a GET request'
        
app.run()