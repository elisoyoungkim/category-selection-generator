from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, world!'

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

# @app.route('/plot1',methods=['POST'])
# def plot1():
#     return render_template('plot1.html')

# @app.route('/plot2',methods=['POST'])
# def plot2():
#     return render_template('plot2.html')

# @app.route('/home',methods=['POST'])
# def next_():
#     return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)