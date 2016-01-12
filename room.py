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
        self.chest = Chest(self.player.level)
        self.monster = Monster()


    def newRoom(self):
        print "You enter a dark room."
        rnd = random.randint(0,10)
        if rnd < 5:
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

    # def inspectRoom(self):
        # if self.hasMonster:
        #
        # if self.hasChest:
