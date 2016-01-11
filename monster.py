from randommonstername import RandomMonsterName
from items import Items
import random

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
        self.level = 1
        self.item = Items()
        self.Loot = self.item.randomWeapon(self.level)

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

    def setLoot(self,value):
        self.Loot = self.item.randomWeapon(value)

    # def setup(self,hp,strength,armor,hasLoot,level):
    #     self.hp = hp
    #     self.strength = strength
    #     self.armor = armor
    #     self.hasLoot = hasLoot
    #     self.level = level
    #     self.setLoot(level)

    def setup(self,difficulty,player_level):
        if difficulty is 1:
            self.hp = random.randint(5,15)
            self.strength = random.randint(1,5)
            self.armor = random.randint(0,5)
            rnd = random.randint(1,10)
            if rnd > 0:
                self.hasLoot = True
            self.level = random.randint(1,6)
            self.setLoot(self.level)

        else:
            self.hp = random.randint(15,25)
            self.strength = random.randint(5,10)
            self.armor = random.randint(2,8)
            rnd = random.randint(0,10)
            if rnd > 7:
                self.hasLoot = True
            self.level = random.randint(1,6)
            self.setLoot(self.level)
