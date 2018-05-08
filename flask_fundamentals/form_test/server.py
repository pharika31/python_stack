from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   # redirects back to the '/' route
   return redirect('/show')
#added for sessions
@app.route('/show')
def show_user():
  return render_template('users.html', name=session['name'], email=session['email'])
app.run(debug=True) # run our server