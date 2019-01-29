import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_WORD"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2', methods =['GET', 'POST'])
def renderPage2():
    print(request.form['anwser1'])
    if "anwser1" not in session:
        session['anwser1'] = request.form['anwser1']
    else:
        return render_template('dontcheat.html')
    return render_template('page2.html')

@app.route('/page3', methods =['GET', 'POST'])
def renderPage3():
    print(request.form['anwser2'])
    if "anwser2" not in session:
        session['anwser2'] = request.form['anwser2']
    else:
        return render_template('dontcheat.html')
    return render_template('page3.html')

@app.route('/final', methods =['GET', 'POST'])
def renderFinal():
    score=0
    print(request.form['anwser3'])
    if "anwser3" not in session:
        session['anwser3'] = request.form['anwser3']
    else:
        return render_template('dontcheat.html')
    if session['anwser1'] == 'Honey':
        score = score +1
    if session['anwser2'] == 'Australia':
        score = score +1
    if session['anwser3'] == 'Hogwarts':
        score = score +1
    return render_template('final.html' , finalScore=score)


@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))

if __name__=="__main__":
    app.run(debug=False)
