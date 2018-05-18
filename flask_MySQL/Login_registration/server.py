from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'ThisisaSecret'
bcrypt = Bcrypt(app)
@app.route('/')
def index():
	return render_template('login.html')

#comes here when user enters login information

@app.route('/login',methods=['POST','GET'])
def login():
	error = False

	if len(request.form['email']) <1:
		flash('Email cannot be blank!','email_login')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email should be in the form abc@email.com','email_login')
		error = True
	else:
		query = "SELECT * from users where email = :email LIMIT 1"
		data = { 'email': request.form['email']}
		print query
		user_data = mysql.query_db(query,data)
		print user_data
		if user_data :
			#store user data in session
			session['user_id'] = user_data[0]['id']
			session['user_f_name'] = user_data[0]['first_name']
			hashed_password = user_data[0]['password']
			if bcrypt.check_password_hash(hashed_password, request.form['password']):
				session['log_status'] = True
				flash("You successfully logged in...")
				return redirect('/success')
			else:
				session['logged_in'] = False
				flash("Login failed!! Try again, or register.","fail")
				return redirect('/')
		else:
			flash("Your email was not found, please try again or register","fail")
			return redirect('/')				


@app.route('/register',methods=['POST','GET'])
def register():
	error = False
	if request.method == 'POST':
		first_name=request.form['f_name']
		last_name = request.form['l_name']
		email = request.form['email']
		password = request.form['password']
		pw_confirm = request.form['pw_confirm']


		
		if len(first_name) <1:
			flash('First name cannot be blank','f_name')
			error = True
		elif len(first_name) <3:
			flash('First name has to be at least 3 characters long','f_name')
			error = True
		if len(last_name) <1:
			flash('Last name cannot be blank','l_name')
			error = True
		elif len(last_name) <2:
			flash('Last name has to be at least 2 characters long','l_name')
			error = True
		if len(email) <1:
			flash('Email cannot be blank','email')
			error = True
		elif not EMAIL_REGEX.match(email):
			flash('Email should be in abc@gmail.com format!')
			error = True
			#check if email already in system
		else:
			query = "select email from users where email= :email"
			data ={
				'email' : request.form['email']
			}
			print query
			result = mysql.query_db(query,data)
			print result
			if result :
				error = True
				flash('Email is already in use!','email')
		if len(request.form['password']) < 1:
			flash('Please enter password!','password')
			error = True
		elif len(request.form['password'] ) < 9:
			flash('Password should have more than 8 characters!','password')
			error = True
		if len(request.form['pw_confirm']) < 1:
			flash('Please re-enter password!','pw_confirm')
			error = True
		elif request.form['pw_confirm']!= request.form['password']:
			flash('Passwords do not match!!!', 'pw_confirm')
			error = True
		if error:
			return redirect('/register')
		else:
			pw_hash = bcrypt.generate_password_hash(password)
			query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :password, now(), now())"
			data ={
				'first_name' : first_name, 
				'last_name' : last_name,
				'email':email,
				'password':pw_hash
			}
			mysql.query_db(query,data)
			session['log_status']=True
			session['user_f_name'] = first_name
			session['user_l_name'] = last_name
			session['user_email'] = email
			return redirect('/success')
	else:
		if request.method == 'GET':
			return render_template('registration.html')


@app.route('/success')
def success():
    #check for session
    if not session['log_status']:
        flash("Your are not logged in, please login or register.")
        return redirect('/')
    else:
        return render_template('success.html')

app.run(debug=True)