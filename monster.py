from randommonstername import RandomMonsterName
from items import Items
from colorama import init, Fore, Back, Style
import random

class Monster(object):

    def __init__(self):
        name = RandomMonsterName()
        self.fullName = name.getFullName()
        self.shortName = name.getShortName()
        self.hp = 10
        self.condition = "normal"
        self.strength = 1
        self.armor = 1
        self.killed = False
        self.hasLoot = False
        self.level = 1
        self.item = Items()
        self.Loot = self.item.randomWeapon(self.level)


    def getFullName(self):
        return self.fullName

    def getShortName(self):
        return self.shortName

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            self.killed = True
            return self.killed

    def killed(killed):
        self.killed = killed

    def takeDamage(self, damage):
        self.hp -= damage
        print Fore.GREEN+self.shortName+": 'AHHHRGWLWLW GROOOWAAR'\n"+Style.RESET_ALL

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.__condition = condition

    def getLoot(self):
        return self.Loot

    def setLoot(self,value):
        self.Loot = self.item.randomWeapon(value)

    def kill(self):
        self.killed = True

    def setup(self,difficulty,player_level):
        if difficulty is 1:
            self.hp = random.randint(5,15)
            self.strength = random.randint(1,5)
            self.armor = random.randint(0,5)
            rnd = random.randint(1,10)
            if rnd > 0:
                self.hasLoot = True
            self.level = random.randint(1,10)
            self.setLoot(self.level)

        else:
            self.hp = random.randint(15,25)
            self.strength = random.randint(5,10)
            self.armor = random.randint(2,8)
            rnd = random.randint(0,10)
            if rnd > 7:
                self.hasLoot = True
            self.level = random.randint(1,6)
            self.setLoot(self.level)


    def attack(self, room, player):
        damage = player.strength + random.randint(0,2)

        if (self.getHP() - damage <= 0):
            room.killMonster()
            player.facesMonster = False
            if self.hasLoot:
                player.addItem(self.getLoot())
                return "You killed %s"%(self.getShortName())+" and it drops some Loot! " +\
                        "Oh look, it's"+Fore.YELLOW+" %s!"%(self.getLoot().name+Style.RESET_ALL)
            else:
                return "You killed %s"%(self.getShortName())
        else:
            self.takeDamage(damage)
            return "You attack" + Fore.GREEN+" %s "%(self.getShortName())+ Style.RESET_ALL +\
             "and you deal" +Fore.RED+" %s "%(damage)+Style.RESET_ALL+"damage.\n"+\
             "The Monster's Health is now at "+Fore.GREEN +str(self.getHP())+Style.RESET_ALL

    def flee(self, room, player):
            player.facesMonster = False
            damage = random.randint(1,15)
            string = Fore.RED +"%s "%(self.getShortName())+ Style.RESET_ALL+"laughs manically as you try to flee from it\n"

            if damage < 5:
                return string +"You barely manage, stumbling through the darkness \n" + \
                 self.player.takeDamage(damage)
            else:
                return string +"As you run through the darkness you fall and hit your head on something. \n" + \
                  self.player.takeDamage(damage)


    def spawn(self,room,player):
        if room.hasMonster:
            if not self.killed and player.facesMonster:
                damage = random.randint(1,15)
                player.takeDamage(damage)
                return "You already face %s, and it attacks you. You take"%(self.getShortName()) + \
                Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n" + \
                "%s, your HP is now at "%(player.name)+ Fore.CYAN + str(player.getHP()) + Style.RESET_ALL +"\n"
            elif room.hasMonster and not self.killed :
                player.facesMonster = True
                damage = random.randint(1,15)
                if(int(player.getHP()) - damage < 0):
                    player.takeDamage(damage)
                    return Style.RESET_ALL, "You took {0} damage, you are now dead".format(damage)
                else:
                    player.takeDamage(damage)
                    return Style.RESET_ALL +"\nA wild" +Fore.GREEN+ " %s "%(self.getFullName()) + \
                    Style.RESET_ALL+ "appears!\n%s attacks and you take"%(self.getShortName()) + \
                    Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n" + \
                    Fore.CYAN +"\n%s"%(player.name)+ Style.RESET_ALL+", your HP is now at "+ Fore.CYAN + str(player.getHP()) + Style.RESET_ALL +"\n"
