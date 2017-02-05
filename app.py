# import the Flask class from the flask module
from flask import Flask,render_template, redirect, url_for, request

# create the application
app = Flask(__name__)

# use decorators to link the function to url
@app.route('/')
def home():
	return render_template('description.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html') # render a template

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Pease try again.'
		else: return redirect(url_for('home'))
	return render_template('login.html', error = error)

@app.route('/plot1',methods=['POST'])
def plot1():
    return render_template('plot1.html')

@app.route('/plot2',methods=['POST'])
def plot2():
    return render_template('plot2.html')

# @app.route('/home',methods=['POST'])
# def next_():
#     return redirect('/')

# start the server with the run() method
if __name__ == '__main__':
	app.run(debug = True)