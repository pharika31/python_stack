from flask import Flask, render_template, request, redirect, session
import random
app= Flask(__name__)
app.secret_key ='ThisisaSecret'

@app.route('/')
def main_page():
	if 'number' not in session:	
		session['number'] = random.randrange(0, 101)
	print session['number']
	if 'message' not in session:	
		session['message'] = ''
	return render_template('index.html', message = session['message'], number = session['number'])

@app.route('/guess', methods=['POST'])
def check_guess():
	user_guess = int(request.form['guess'])
	print user_guess
	print session['number']
	if user_guess < session['number']:
		session['message'] = "Too low!"
	if user_guess > session['number']:
		session['message'] = "Too High!"

	if user_guess == session['number']:
		session['message'] = "{}".format(user_guess)+ " was the number"

	return render_template('index.html', message = session['message'], number = session['number'])

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('number')
	session.pop('message')
	return redirect('/')

app.run(debug=True)