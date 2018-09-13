from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
#from flask import jsonify
#from business import controlLed

app = Flask(__name__)

#@app.route('/')
#def loing_form():
	#return render_template('login.html')

#@app.route('/login', methods=['GET','POST'])
#def login():
	#if request.method =='POST':
		#name = request.form['username']
		#pwd = request.form['password']
		#print(name)
		#print(pwd)
		#return redirect(url_for('reMain_form'))

@app.route('/')
def reMain_form():
	return render_template('main.html')

@app.route('/control', methods=['GET','POST'])
def control():
	if request.method =='POST':
		return redirect(url_for('sleep'))

@app.route('/sleep')
def sleep():
	return render_template('sleep.html')

@app.route('/set', methods=['GET','POST'])
def set():
	if request.method =='POST':
		return redirect(url_for('times'))

@app.route('/times')
def times():
	return render_template('times.html')

@app.route('/back', methods=['GET','POST'])
def back():
	if request.method =='POST':
		return redirect(url_for('sleep'))

if __name__=='__main__':
	app.run(host='0.0.0.0', port=80)

#@app.route('/control', methods=['GET','POST'])
#def controlled():
	#if request.method == 'POST':
		#value = request.form['value']
		#device = request.form['device']
		#msg = device + ':' + value
		#print(msg)
		#controlLed(device,value)
		#return jsonify({'data':'50'})



