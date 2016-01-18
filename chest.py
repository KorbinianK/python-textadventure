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
        print "You found "+Fore.YELLOW+self.Loot.name+Style.RESET_ALL+"! It has been added to your"+Fore.CYAN+" inventory "+Style.RESET_ALL+"."
        return self.Loot

    def is_opened(self):
        return self.opened

    def open(self,player):
        print "The chest opens with a loud squeaky noise"
        self.opened = True
        if self.hasLoot:
            return self.player.addItem(self.getLoot())

        else:
            string = "You open the chest. It's empty."

        return string

    def has_loot(self):
        return self.hasLoot
