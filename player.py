class Player(object):

    def __init__(self):
    	self.name = "a"
        self.hp = 100
        self.facesMonster = False
        self.victory = False
        self.condition = "normal"
        self.strength = 15
        self.armor = 1
        self.inventory =[]

    def is_alive(self):
        return self.hp > 0

    def takeDamage(self, damage):
        self.hp -= damage

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.condition = condition

    def is_facing_Monster(self):
        return self.facesMonster

    def facing_Monster(self, status):
        self.facesMonster = status

    def addItem(self, item):
        self.inventory.append(item)

    def printInventory(self):
        return str(self.inventory[0].name)
