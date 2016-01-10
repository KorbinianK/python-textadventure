from colorama import init, Fore, Back, Style
init()

class Player(object):
    def __init__(self, name):
    	self.name=name
        self.hp = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def takeDamage(self, damage):
        self.hp -= damage

    def getHP(self):
        return self.hp
    