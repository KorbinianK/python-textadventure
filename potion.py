class potion(item):
	
	def __init__(self, name, value, strength):
		super().__init__(name, value)
		self.strength=strength
		
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

	def setStrength(self, strength):
		self.strength=strength