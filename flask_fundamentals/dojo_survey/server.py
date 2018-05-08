from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def root_route():
	return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
	result = request.form
	return render_template("result.html",result=result)
app.run(debug=True)