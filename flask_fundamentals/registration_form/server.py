from flask import Flask, redirect, request, session, flash, render_template
import re, datetime
app = Flask(__name__)
app.secret_key = 'ThisisaSecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def evaluate_form():
	error = False
	if len(request.form['f_name']) < 1:
		flash('Please enter First name!', 'f_name')
		error = True
	elif not request.form['f_name'].isalpha():
		flash('First name cannot have numbers','f_name')
		error = True
	if len(request.form['l_name']) < 1:
		flash('Please enter Last name!','l_name')
		error = True
	elif not request.form['f_name'].isalpha():
		flash('Last name cannot have numbers','l_name')
		error = True
	if len(request.form['email']) < 1:
		flash('Please enter Email!', 'email')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!",'email') 
		error = True
	if len(request.form['password']) < 1:
		flash('Please enter password!','password')
		error = True
	elif len(request.form['password'] ) < 9:
		flash('Password should have more than 8 characters!','password')
		error = True
	if len(request.form['pw_confirm']) < 1:
		flash('Please enter password!','password')
		error = True
	elif request.form['pw_confirm']!= request.form['password']:
		flash('Passwords do not match!!!', 'pw_confirm')
		error = True
	if error == True:
		return redirect('/')
	else:
		flash("Thanks for submitting the form!","success")
	return redirect('/') 
	
app.run(debug=True)