# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/login')
def logiin():
  return render_template('login.html')

@app.route('/')
@app.route('/homepage')
def homepage():
  return render_template('homepage.html')

@app.route('/')
@app.route('/aboutus')
def aboutus():
  return render_template('aboutus.html')

@app.route('/')
@app.route('/donate')
def donate():
  return render_template('donate.html')

@app.route('/')
@app.route('/locator')
def locator():
  return render_template('locator.html')

@app.route('/locator', methods = ['GET', 'POST'])
def handle_Input():
  if request.method == 'GET':
    return f"Hi! These are the nearest food banks in {str(place)}." 
  else:
    return "Invalid input."

# @app.route('/donate', methods = ['GET', 'POST'])
# def handle_Input():
 
  
    
 


app.run(host='0.0.0.0', port=81, debug=True)
