import plotly.graph_objects as go
from flask import Flask, render_template
from jinja2 import Template, Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def home():
    data = [go.Bar(x=[1,2,3],y=[1,2,3])]
    layout = go.Layout(title = 'My Plot')
    fig = go.Figure(data=data, layout=layout)
    plot_html = fig.to_html(full_html=False)
    return render_template('index.html',plot_html=plot_html)

app.run()

'''
y = [getSumA's, getSumB's, getSumC's, getSumD's,getSumF]
x = ['a','b','c','d','f']       
'''