

import random, time,sys
from random import uniform
from stringhandler import Stringhandler

class ByteBoss(object):

    def __init__(self):
        self.name = "Megabyte"
        self.isBoss = True
        self.hp = 128
        self.strength = 8
        self.killed = False
        self.handler = Stringhandler()

    def kill(self):
        self.killed = True

    def takeDamage(self,damage,player):
        self.hp -= damage

    def getHP(self):
        return self.hp

    def calcDamage(self):
        damage = self.strength + random.randint(0,3)
        return damage
    # def attack(self,player,damage):

    def attackFromPlayer(self,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.hp - damage <= 0):
            self.kill()
            player.facesBoss = False
            return self.handler.strBoss("bDie",player,damage)
        else:
            self.takeDamage(damage,player)
            return self.handler.strBoss("bHit",player,damage)

    def spawn(self,player):

        player.facesBoss = True
        damage = self.calcDamage()
        print self.handler.strBoss("bSpawn",player,None)

        return self.handler.strBoss("bSpawn",player,None)

class HipsterBoss(object):

    def __init__(self):
        self.name = "the Hipster"
        self.isBoss = True
        self.hp = 128
        self.strength = 8
        self.killed = False
        self.handler = Stringhandler()

    def kill(self):
        self.killed = True

    def takeDamage(self,damage,player):
        self.hp -= damage

    def getHP(self):
        return self.hp

    def calcDamage(self):
        damage = self.strength + random.randint(0,3)
        return damage
    # def attack(self,player,damage):

    def attackFromPlayer(self,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.hp - damage <= 0):
            self.kill()
            player.facesBoss = False
            return self.handler.strBoss("hDie",player,damage)
        else:
            self.takeDamage(damage,player)
            return self.handler.strBoss("hHit",player,damage)

    def spawn(self,player):

        player.facesBoss = True
        damage = self.calcDamage()
        print self.handler.strBoss("hSpawn",player,None)

        return self.handler.strBoss("hSpawn",player,None)
