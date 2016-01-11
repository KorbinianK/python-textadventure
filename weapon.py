class Weapon(object):

	def __init__(self):
		# super().__init__(name, value)
		self.damage=1
		self.name = "name"
		self.value = 1
		self.isBroken=False

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

	def setDamage(self, damage):
		self.damage=damage

	def destroy(self):
		self.isBroken=true

	def isBroken(self):
		return self.isBroken
