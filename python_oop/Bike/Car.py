class Car(object):
	def __init__(self,price,speed,fuel,mileage):

		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.mileage=mileage
		if price >10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print "Price: %d"%(self.price)
		print "Speed: %d mph"%(self.speed)
		print "Fuel: %s"%(self.fuel)
		print "Mileage:%d mpg"%(self.mileage)
		print "Tax: %.2f"%(round(self.tax,2))


car1 = Car(5000,45,"Full",100)
car2 = Car(15000,55,"Not Full",100)
car3 = Car(12000,65,"Full",100)
car4 = Car(20000,75,"Kind of Full",100)
car5 = Car(30000,85,"Full",100)
car6 = Car(7000,100,"Not Full",100)
