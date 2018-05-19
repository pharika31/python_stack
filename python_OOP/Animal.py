class Animal(object):
	def __init__(self,name,health):
		self.name=name
		self.health=health
	def walk(self):
		self.health -=1
		return self
	def run(self):
		self.health -=5
		return self
	def display_health(self):
		print "Animal : ",self.name
		print "Health: %d"%(self.health)
		return self

cat = Animal("cat",20)
cat.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self,name):
		super(Dog, self).__init__(name,150 )   
		 
	def pet(self):
		self.health +=5
		return self

dog1 = Dog('Lab')
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
	
	def __init__(self,name):
		super(Dragon, self).__init__(name, 170)    
		  

	def fly(self):
		self.health -=10
		return self
	def display_health(self):
		super(Dragon, self).display_health()
		print "I am  a dragon"

dragon = Dragon('dragon')
dragon.fly().display_health()