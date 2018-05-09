from flask import Flask, render_template, request, redirect, session
import random
app= Flask(__name__)
app.secret_key ='ThisisaSecret'

@app.route('/')
def main_page():
	session['number'] = random.randrange(0, 101)
	print session['number']
	return render_template('index.html')

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
	return render_template('index.html', message = session['message'])

app.run(debug=True)