from flask import Flask, render_template, request, redirect, session
import random, datetime
app= Flask(__name__)
app.secret_key ='ThisisaSecret'

def generate_random(start, end):
	return random.randrange(start,end)

def checkEarnedOrLost():
	val = random.randrange(0,2)
	if val == 1:
		return True
	else:
		return False

def addActivity(number, building, result):
	timestamp = datetime.datetime.now()
	if building == 'farm':
		session['activity'].append(['earn', 'Earned %d from the %s! %s' % (number, building, timestamp)])

	elif building == 'cave':
		session['activity'].append(['earn', 'Earned %d from the %s! %s' % (number, building, timestamp)])
	elif building == 'house':
		session['activity'].append(['earn', 'Earned %d from the %s! %s' % (number, building, timestamp)])

	elif building == 'casino':
		if result == 'Earned':
			session['activity'].append(['earn', 'Earned %d from the %s! %s' % (number, building, timestamp)])
		elif result == 'Lost':
			session['activity'].append(['lost', 'Entered a casino and lost %d golds... Ouch %s' %(number, timestamp)])
	else:
		print "OOps!! Something is wrong!"



@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
		print session['gold']
	if 'activity' not in session:
		session['activity'] = []
	return render_template('index.html', gold = session['gold'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def process_money():
	building = request.form['building']
	if  building== "farm":
		farm_gold = generate_random(10, 20)
		session['gold'] += farm_gold
		addActivity(farm_gold, 'farm', 'Earned')
	elif  building== "cave":
		cave_gold = generate_random(5, 10)
		session['gold'] += cave_gold
		addActivity(cave_gold, 'cave', 'Earned')
	elif  building== "house":
		house_gold = generate_random(2, 5)
		session['gold'] += house_gold
		addActivity(house_gold, 'house', 'Earned')

		''' earned here is True, Lost is False'''
	elif building == "casino":
		result  = checkEarnedOrLost()
		casino_gold = generate_random(0,50)
		if result:
			session['gold'] += casino_gold
			addActivity(casino_gold, 'casino', 'Earned')

		else:
			session['gold'] -= casino_gold
			addActivity(casino_gold, 'casino', 'Lost')
	else:
		print "Error - Something is wrong dude!"
	return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['activity'] = []
    return redirect('/')


app.run(debug=True)