from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'ThisisaSecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():

	return render_template('index.html')
@app.route('/email',methods=['POST'])
def add_email():
	error = False

	if len(request.form['email']) <1:
		flash('Email cannot be blank!','email')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email should be in the form abc@email.com','email')
		error = True
	else:
		
		query = "select email from emails where email= :email"
		data ={
			'email' : request.form['email']
		}
		print query
		result = mysql.query_db(query,data)
		print result
		if result :
			error = True
			flash('Email is already in use!','email')
		
	if error==True:
		return redirect('/')
	else:
		flash('The email address (' + request.form['email'] +') is a VALID email address! Thank You!' , 'success')
		query = "INSERT into emails (email, created_at ) values (:email, NOW())"
		data ={
		'email' : request.form['email']
		}
		mysql.query_db(query,data)
		print "Inserted new email"

		return redirect('/success')

@app.route('/success')
def insert_email():
	
	#to show all the values in database:

	query = "SELECT email, created_at FROM emails"
	all_emails = mysql.query_db(query)
	return render_template('success.html', all_email = all_emails)

app.run(debug=True)


