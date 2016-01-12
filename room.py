from monster import Monster
from chest import Chest
import random

class Room(object):

    def __init__(self,difficulty,player):
        self.hasMonster = False
        self.hasChest = True
        self.isDone = False
        self.difficulty = difficulty
        self.player = player
        self.chest = Chest(self.player)
        self.monster = Monster()
        self.inspected = False


    def newRoom(self):
        print '{:^80}'.format("###################################")
        print '{:^80}'.format("You enter a dark room.")
        print '{:^80}'.format("###################################")
        rnd = random.randint(0,10)
        if rnd < 1:
            self.hasMonster = True
        else:
            self.hasChest = True
        if self.hasMonster:
            if self.difficulty == "easy":
                self.monster.setup(1,self.player.level)
            else:
                self.monster.setup(2,self.player.level)
        if self.hasChest:
            if self.difficulty == "easy":
                self.chest.level = random.randint(1,10)
            else:
                self.chest.level = random.randint(1,10)
        else:
            self.isDone = True

    def inspectRoom(self):
        self.inspected = True

    def killMonster(self):
        self.monster.kill()
        self.hasMonster = False
