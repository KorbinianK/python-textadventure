from items import Items
from colorama import init, Fore, Back, Style
from stringhandler import Stringhandler
import random

class Chest(object):

    def __init__(self,player):
        name = "item"
        self.opened = False
        self.player = player
        self.level = player.level
        self.item = Items()
        self.handler = Stringhandler()
        self.hasLoot = True
        if self.level > 5:
            self.Loot = self.item.randomWeapon(self.level)
        else:
            rnd = random.randint(0,10)
            if rnd < 3:
                self.hasLoot = False
                self.Loot = ""
            else:
                self.Loot = self.item.randomWeapon(self.level)

    def getLoot(self):
        return self.Loot

    def is_opened(self):
        return self.opened

    def open(self,player):
        self.opened = True
        player.lvlUp()
        if self.hasLoot:
            return self.handler.strChest("open",self.getLoot().name)+"\n"+self.player.addItem(self.getLoot())
        else:
            string = self.handler.strChest("empty",self.getLoot())

        return string

    def has_loot(self):
        return self.hasLoot
