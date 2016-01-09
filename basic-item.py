class Item(object):
	def __init__(self, name, value):
		self.name=name
		self.value=value

	def __str__(self):
		return ""

	def getName(self):
		return self.name

	def getValue (self):
		return self.value

	def setName(self, name):
		self.name=name

	def setValue(self, value):
		self.value=value


