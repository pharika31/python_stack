from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def home():
	return render_template('index.html')

@app.route('/ninja')

def display_ninjas():
	return render_template('ninjas.html')

@app.route('/ninja/<color>')

def display_colorninja(color):
	return render_template('color.html',colour=color)
app.run(debug=True)