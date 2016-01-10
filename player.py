from colorama import init, Fore, Back, Style
init()

#
#
#
#

class Player(object):
    def __init__(self):
        self.hp = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def takeDamage(self, damage):
        self.hp -= damage
        print("\nYou slap yourself in the face \n"+"Your HP is now at " + Fore.RED + str(self.hp) +"\n"  )
        print(Style.RESET_ALL)

    def returnHP(self):
        return Fore.RED + str(self.hp) + (Style.RESET_ALL)
