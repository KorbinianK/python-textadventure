class Potion(object):

	def __init__(self, name, strength):
		self.strength=strength
		self.name=name

	def __str__(self):
		return ""

	def setName(self, name):
		self.name=name

	def setValue(self, value):
		self.value=value

	def setStrength(self, strength):
		self.strength=strength
