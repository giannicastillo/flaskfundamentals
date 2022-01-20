from cgitb import reset
from os import name
from flask import Flask, render_template, redirect, session, request
app= Flask (__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def nextPage():
    # name= request.form['name']
    session['name']=request.form['name']
    session["Locations"]=request.form['Locations']
    session['Languages']= request.form['Languages']
    session['Comments']=request.form['Comments']
    return render_template('result.html')




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'


if __name__=="__main__":
    app.run(debug=True)