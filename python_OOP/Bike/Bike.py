class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles=0
	
	def displayInfo(self):
		print "price is %d , maximum speed is %d mph, total miles: %d "%(self.price , self.max_speed, self.miles)
		return self
	def ride(self):
		print "Riding"
		self.max_speed += 10
		return self
	def reverse(self):
		print "Reversing!"
		self.max_speed -= 10 
		return self

bike1 = Bike(200, 25)
bike2 = Bike(300, 35)
bike3 = Bike(400, 45)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()