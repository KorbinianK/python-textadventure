from items import Items

class Chest(object):

    def __init__(self,level):
        name = "item"
        self.opened = False
        self.level = level
        self.item = Items()
        self.Loot = self.item.randomWeapon(self.level)

    def getLoot(self):
        return self.Loot

    def is_opened(self):
        return self.opened

    def open(self):
        print "The chest opens with a loud squeaky noise"
        self.opened = True
        return self.getLoot()
