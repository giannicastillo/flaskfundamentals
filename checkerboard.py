from ast import Num
from os import times
from turtle import color
from flask import Flask, render_template
app= Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html",y=8, x=8)

@app.route('/<int:num>')
def squares(num):
    print ("index.html",'/css/style.css')
    return render_template("index.html", x=num, y=8)

@app.route('/<int:num>/<int:num2>')
def squares2(num,num2):
    print ("index.html",'/css/style.css')
    return render_template("index.html", x=num, y=num2)
@app.route('/<int:x>/<color>')

def colors(x,color):
    print ('index.html', color)
    return render_template("index.html",x=x, color=color)




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'


if __name__=="__main__":
    app.run(debug=True)