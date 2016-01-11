from randommonstername import RandomMonsterName
from items import Items

class Monster(object):

    def __init__(self):
        name = RandomMonsterName()
        self.fullName = name.getFullName()
        self.shortName = name.getShortName()
        self.hp = 10
        self.condition = "normal"
        self.strength = 1
        self.armor = 1
        self.killed = False
        self.hasLoot = False
        item = Items()
        self.Loot = item.randomWeapon()

    def getFullName(self):
        return self.fullName

    def getShortName(self):
        return self.shortName

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            self.killed = True
            return self.killed

    def killed(killed):
        self.killed = killed

    def takeDamage(self, damage):
        self.hp -= damage
        return self.shortName+": 'AHHHRGWLWLW GROOOWAAR'\n"+"The monster takes %s damage"%(damage)

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.__condition = condition

    def getLoot(self):
        return self.Loot
