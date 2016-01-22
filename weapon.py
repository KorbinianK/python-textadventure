class Weapon(object):

	def __init__(self):
		self.damage=1
		self.name = ""
		self.nameshort =""

	def getName(self):
		return self.name

	def setDamage(self, damage):
		self.damage=damage
