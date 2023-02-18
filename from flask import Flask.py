from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def rootPage():
    height = ''
    weight = ''
    bmi = ''
    if request.method == "POST" and 'weight' in request.form:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        bmi = calcBmi(height, weight)
    return render_template("index.html", height=height, weight=weight, bmi=bmi)

def calcBmi(height, weight):
    return round((703* weight) / (height)**2,2)

#flask by deault accepts get methods, must declare if u want more
@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return 'You have used a post request!'
    else:
        return 'Likely a GET request'
        
app.run()