from items import Items
from colorama import init, Fore, Back, Style
import random

class Chest(object):

    def __init__(self,player):
        name = "item"
        self.opened = False
        self.player = player
        self.level = player.level
        self.item = Items()
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
        if self.hasLoot:
            return "You found "+Fore.YELLOW+self.Loot.name+Fore.WHITE+\
            "! It has been added to your"+Fore.CYAN+" inventory "+Fore.WHITE+".\n"+\
            self.player.addItem(self.getLoot())

        else:
            string = "It's empty."

        return string

    def has_loot(self):
        return self.hasLoot
