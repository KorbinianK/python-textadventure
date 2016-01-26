from colorama import init, Fore, Back, Style
from randommonstername import RandomMonsterName
from items import Items
import random, time,sys
from random import uniform
from stringhandler import Stringhandler

class Monster(object):

    def __init__(self):
        name = RandomMonsterName()
        self.fullName = name.getFullName()
        self.shortName = name.getShortName()
        self.hp = 10
        self.strength = 1
        self.killed = False
        self.hasLoot = False
        self.level = 1
        self.item = Items()
        self.Loot = self.item.randomWeapon(self.level)
        self.handler = Stringhandler()

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

    def takeDamage(self, damage,player):
        self.hp -= damage
        string = '"'+self.handler.strMonster("hit",self,player)+'"\n'
        for char in string:
            time.sleep(uniform(0.01, 0.05))
            sys.stdout.write('\033[35m'+'\033[1m'+char)
            sys.stdout.flush()
        print Fore.WHITE

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.__condition = condition

    def getLoot(self):
        return self.Loot

    def setLoot(self,value):
        self.Loot = self.item.randomWeapon(value)

    def kill(self):
        self.killed = True

    def calcDamage(self):
        damage = self.strength + random.randint(0,3)
        return damage

    def setup(self,difficulty,player_level):
        self.killed = False
        if difficulty is 1:
            self.hp = player_level + random.randint(10,25)
            self.strength = player_level + random.randint(1,9)
            rnd = random.randint(0,10)
            if rnd > 3:
                self.hasLoot = True
            self.level = random.randint(1,10)
            self.setLoot(self.level)

        else:
            self.hp = player_level + random.randint(15,35)
            self.strength = player_level + random.randint(5,15)

            rnd = random.randint(0,10)
            if rnd > 7:
                self.hasLoot = True
            self.level = random.randint(1,6)
            self.setLoot(self.level)


    def attackPlayer(self,room,player):
        damage = self.calcDamage()
        return player.takeDamage(damage,room.monster)

    def attack(self,room,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.hp - damage <= 0):
            room.killMonster()
            player.facesMonster = False
            if self.hasLoot:
                return self.handler.strMonster("killedLoot",self,player)+"\n"+player.addItem(self.getLoot())
            else:
                return self.handler.strMonster("killed",self,player)

        else:
            self.takeDamage(damage,player)
            return self.handler.strMonsterDamage("getAttacked",self,damage,player) +"\n"+\
            self.handler.strMonsterDamage("returnHP",self,damage,player) +"\n"+self.attackPlayer(room,player)

    def flee(self, room, player):
            player.facesMonster = False
            damage = self.calcDamage()

            if damage < 5:
                return self.handler("flee",self,player) +" "+ self.handler("fleeSuccess",self,player)
            else:
                return self.handler("flee",self,player) +" "+ self.handler("fleeFail",self,player) +"\n" + player.takeDamage(damage,room.monster)


    def spawn(self,room,player):
        if room.hasMonster:
            if not self.killed and player.facesMonster:
                response="something went wrong"
                return response
            elif room.hasMonster and not self.killed :
                player.facesMonster = True
                damage = self.calcDamage()
                return self.handler.strMonsterDamage("spawn",self,damage,player)+"\n"+\
                player.takeDamage(damage,room.monster)
