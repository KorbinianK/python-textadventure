from weapon import Weapon
from potion import Potion

class Items():

    def __init__(self):
        self.weapon = Weapon()
        self.potion = Potion()


    def randomWeapon(self, value):
        if value < 5:
            self.weapon.name = "a Knife"
            self.weapon.nameshort = "Knife"
            self.weapon.damage = 4
            return self.weapon
        if value <7:
            self.weapon.name = "a Shoe"
            self.weapon.nameshort ="Shoe"
            self.weapon.damage = 2
            return self.weapon
        else:
            self.weapon.name = "a Sword"
            self.weapon.nameshort ="Sword"
            self.weapon.damage = 6
            return self.weapon

    def newPotion(self,strength,uses):
        self.potion.strength = strength
        self.potion.uses = uses
        return self.potion
