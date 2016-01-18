class Potion(object):

	def __init__(self):
		self.strength=0.2
		self.name= "a Potion"
		self.uses = 5
		self.isEmpty = False


	def drink(self):
		if self.uses > 0:
			self.uses = self.uses - 1
		else:
			self.isEmpty = True
