
import bosslist as Bosslist
from bosslist import ByteBoss,HipsterBoss
import random, time,sys
from random import uniform
from stringhandler import Stringhandler

class Endboss(object):

    def __init__(self):

        self.hp = 10
        self.strength = 10
        self.killed = False
        self.handler = Stringhandler()
        self.bossList = []
        self.byteBoss = Bosslist.ByteBoss()
        self.hipsterBoss = Bosslist.HipsterBoss()
        self.boss = None

    def randomBoss(self,player):
        self.bossList.append(self.byteBoss)
        self.bossList.append(self.hipsterBoss)
        # self.bossList.append("")
        # self.bossList.append("")
        self.boss = random.choice(self.bossList)
        return self.boss

    def kill(self):
        self.boss.killed = True

    def takeDamage(self,damage,player):
        self.boss.hp -= damage

    def getHP(self):
        return self.boss.hp

    def calcDamage(self):
        damage = self.boss.strength + random.randint(0,3)
        return damage

    def attackFromPlayer(self,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.boss.hp - damage <= 0):
            self.kill()
            player.facesBoss = False
            player.victory = True
            if isinstance(self.boss,ByteBoss):
                return self.handler.strBoss("bDie",player,damage)
            elif isinstance(self.boss,HipsterBoss):
                return self.handler.strBoss("hDie",player,damage)
            else:
                return "Error 404: Boss not found"
        else:
            self.takeDamage(damage,player)

            if isinstance(self.boss,ByteBoss):

                return self.handler.strBoss("bHit",player,damage)+"\n"+self.attack(player)
            elif isinstance(self.boss,HipsterBoss):
                return self.handler.strBoss("hHit",player,damage)+"\n"+self.attack(player)

    def attack(self,player):
        damage = self.calcDamage()
        if isinstance(self.boss,ByteBoss):
            return self.handler.strBoss("bAttack",player,damage)+player.takeDamage(damage,self.boss)
        elif isinstance(self.boss,HipsterBoss):
            return self.handler.strBoss("hAttack",player,damage)+player.takeDamage(damage,self.boss)

    def spawn(self,player):
        player.facesBoss = True
        damage = self.calcDamage()
        if isinstance(self.boss,ByteBoss):
            return self.handler.strBoss("bSpawn",player,damage)
        elif isinstance(self.boss,HipsterBoss):
            return self.handler.strBoss("hSpawn",player,damage)
