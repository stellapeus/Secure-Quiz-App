import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "animalName" not in session:
        session["animalName"]=request.form['animalName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "musicGenre" not in session:
        session["musicGenre"]=request.form['musicGenre']
    return render_template('page3.html')
    
@app.route('/page',methods=['GET','POST'])
def renderPage():
    if "favHoliday" not in session:
        session["favHoliday"]=request.form['favHoliday']
    pointCount = 0
    if session["favHoliday"] == "christmas":
        pointCount = pointCount +1
    if session["musicGenre"] == "pop":
        pointCount = pointCount +1
    if session["animalName"] == "giraffe":
        pointCount = pointCount +1
    return render_template('page.html', pointCount=pointCount)
    
if __name__=="__main__":
    app.run(debug=False)
