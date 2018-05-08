from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/')
def main_page():
	try:
    		session['counter'] +=1
	except KeyError:
    		session['counter'] =1
	return render_template('index.html',count = session['counter'])

@app.route('/increment', methods=['POST'])
def reload_page_increment2():
	session['counter'] +=1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_to_1():
	session['counter'] =0
	return redirect('/')
app.run(debug=True)