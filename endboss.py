
import bosslist as Bosslist
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

    def randomBoss(self,player):
        self.bossList.append(self.byteBoss)
        # self.bossList.append("")
        # self.bossList.append("")
        # self.bossList.append("")
        boss = random.choice(self.bossList)
        
        return boss

    # def setupBoss(self,player):

    def kill(self):
        self.killed = True
