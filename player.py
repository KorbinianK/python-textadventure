class Player(object):

    def __init__(self, name):
    	self.name=name
        self.hp = 100
        self.facesMonster = False
        self.victory = False
        self.condition = "normal"
        self.strength = 1
        self.armor = 1

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
