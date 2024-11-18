import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import time

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
    session["starttime"]=time.time()
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "highestPop" not in session:
        session["highestPop"]=request.form['highestPop']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "biggestCountry" not in session:
        session["biggestCountry"]=request.form['biggestCountry']
    return render_template('page3.html')
    
@app.route('/page',methods=['GET','POST'])
def renderPage():
    session["endtime"]=time.time()
    timeTaken=session["endtime"] - session["starttime"]
    if "pyramidsLocation" not in session:
        session["pyramidsLocation"]=request.form['pyramidsLocation']
    pointCount = 0
    if session["pyramidsLocation"] == "egypt" or session["pyramidsLocation"] == "Egypt":
        pointCount = pointCount +1
    if session["biggestCountry"] == "russia" or session["biggestCountry"] == "Russia":
        pointCount = pointCount +1
    if session["highestPop"] == "india" or session["highestPop"] == "India":
        pointCount = pointCount +1
    return render_template('page.html', pointCount=pointCount, timeTaken=timeTaken)
    
if __name__=="__main__":
    app.run(debug=False)
