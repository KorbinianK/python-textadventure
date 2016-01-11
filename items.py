from weapon import Weapon

class Items():

    weapon = Weapon()

    def randomWeapon(self):

        self.weapon.name = "a Knife"
        self.weapon.setValue = 1
        self.weapon.setDamage = 2
        return self.weapon
