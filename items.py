from weapon import Weapon

class Items():

    weapon = Weapon()

    def randomWeapon(self, value):
        if value < 3:
            self.weapon.name = "a Knife"
            self.weapon.setValue = 1
            self.weapon.setDamage = 2
            return self.weapon
        else:
            self.weapon.name = "a Sword"
            self.weapon.setValue = 5
            self.weapon.setDamage = 10
            return self.weapon
