from weapon import Weapon
from gold import Gold

class Items():

    def __init__(self):
        self.weapon = Weapon()
        #self.gold = Gold()

    def randomWeapon(self, value):
        if value < 5:
            self.weapon.name = "a Knife"
            self.weapon.setValue = 1
            self.weapon.setDamage = 2
            return self.weapon
        if value <7:
            self.weapon.name = "a Shoe"
            self.weapon.setValue = 1
            self.weapon.setDamage = 2
            return self.weapon
        else:
            self.weapon.name = "a Sword"
            self.weapon.setValue = 5
            self.weapon.setDamage = 10
            return self.weapon
