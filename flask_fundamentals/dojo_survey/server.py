from flask import Flask, render_template, request, flash, session, redirect
import re

app = Flask(__name__)
app.secret_key ='ThisisaSecret'

@app.route('/')
def root_route():
	return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
	errors = False
	if len(request.form['name']) < 1:
		flash("Name cannot be blank!","nameError")
		errors = True
	
	elif len(request.form['comment']) < 1:
		flash("Comment cannot be blank!","commentError")
		errors = True
	elif len(request.form['comment']) < 1:
		flash("Comment cannot be more than 120 characters!","commentError")
		errors = True
	
	if errors == True:
		return redirect('/')
	else:
		result = [['Name', request.form['name']], ['Location', request.form['loc']], ['Language',request.form['lang']], ['Comment', request.form['comment']]]
		return render_template("result.html",result=result)
app.run(debug=True)