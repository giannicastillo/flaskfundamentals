from cgitb import reset
from flask import Flask, render_template, redirect, session, request
app= Flask (__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "count" not in session:
        session["count"]=0
    return render_template('index.html')

@app.route('/process_count')
def count_up():
    session ["count"] +=1
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')













@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'


if __name__=="__main__":
    app.run(debug=True)