class Product(object):
	def __init__(self, price,item_name,item_weight, brand, status="for sale"):
		self.price=price
		self.item_name = item_name
		self.item_weight = item_weight
		self.brand = brand
		self.status=status
	def sell(self):
		self.status="sold"
		return self
	def add_tax(self,tax):
		self.price += tax*self.price
		return self.price
	def Return(self,reason):
		if reason=="defective":
			self.status = "defective"
			self.price=0
		elif reason=="in a box":
			self.status = "For Sale"
		elif reason=="open box":
			self.status = 'Used'
			self.price = self.price - (self.price * 0.2)
		return self
	def display_all(self):
		print "Price is : %d"%(self.price)
		print "Item Name: ", self.item_name
		print "Weight: %d g"%(self.item_weight)
		print "Brand: ", self.brand
		print "Status: ", self.status
		return self

#testing:
milk = Product(4,"organic milk",250,"Stonyfield")

milk.display_all()
print milk.add_tax(0.12)
milk.sell().Return("defective").display_all()