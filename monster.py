from randommonstername import RandomMonsterName
from items import Items
from colorama import init, Fore, Back, Style
import random, time,sys

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


    def attackPlayer(self,room,player):
        damage = self.strength
        if player.triedWalk:
            player.triedWalk = False

            for x in range (0,5):
                b = "You carefully walk through the darkness towards the monster." + "." * x
                sys.stdout.write('\r'+b)
                time.sleep(0.3)
            print "\n"
        print Fore.GREEN+str(self.getShortName())+Style.RESET_ALL+" strikes and hits you in the face.\n"
        return player.takeDamage(damage,room.monster)

    def attack(self,room,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.hp - damage <= 0):
            room.killMonster()
            player.facesMonster = False

            if self.hasLoot:

                return "You killed %s"%(self.getShortName())+" and it drops some Loot! " +\
                        "Oh look, it's"+Fore.YELLOW+" %s!"%(self.getLoot().name+Style.RESET_ALL) +"\n" +player.addItem(self.getLoot())
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
            time.sleep(0.5)
            if damage < 5:
                return string +"You barely manage, stumbling through the darkness \n" + \
                 player.takeDamage(damage,room.monster)
            else:
                return string +"As you run through the darkness you fall and hit your head on something. \n" + \
                  player.takeDamage(damage,room.monster)


    def spawn(self,room,player):
        if room.hasMonster:
            if not self.killed and player.facesMonster:
                damage = random.randint(1,15)

                if int(player.getHP())-damage >=0:
                    player.takeDamage(damage,room.monster)
                    response="You already face %s, and it attacks you."%(self.getShortName())

                else:
                    response="something went wrong"
                return response
            elif room.hasMonster and not self.killed :
                player.facesMonster = True
                damage = random.randint(1,15)
                if(int(player.getHP()) - damage < 0):
                    player.takeDamage(damage,room.monster)
                    return Style.RESET_ALL, "You took {0} damage, you are now dead".format(damage)
                else:
                    player.takeDamage(damage,room.monster)
                    return Style.RESET_ALL +"\nA wild" +Fore.GREEN+ " %s "%(self.getFullName()) + \
                    Style.RESET_ALL+ "appears!\n%s attacks and you take"%(self.getShortName()) + \
                    Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n" + \
                    Fore.CYAN +"\n%s"%(player.name)+ Style.RESET_ALL+", your HP is now at "+ Fore.CYAN + str(player.getHP()) + Style.RESET_ALL +"\n"
