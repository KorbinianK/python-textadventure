from randommonstername import RandomMonsterName
from items import Items
from colorama import init, Fore, Back, Style
import random, time,sys
from random import uniform
from stringhandler import Stringhandler

class Monster(object):

    def __init__(self):
        name = RandomMonsterName()
        self.fullName = name.getFullName()
        self.shortName = name.getShortName()
        self.hp = 10
        self.strength = 1
        self.killed = False
        self.hasLoot = False
        self.level = 1
        self.item = Items()
        self.Loot = self.item.randomWeapon(self.level)
        self.handler = Stringhandler()

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
        #print Fore.GREEN+self.shortName+":"
        string = '"'+self.handler.strMonster("hit",self,None)+'"\n'
        for char in string:
            time.sleep(uniform(0.01, 0.05))
            sys.stdout.write('\033[35m'+'\033[1m'+char)
            sys.stdout.flush()
        print Fore.WHITE

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
            self.hp = player_level + random.randint(5,15)
            self.strength = player_level + random.randint(1,5)
            rnd = random.randint(1,10)
            if rnd > 3:
                self.hasLoot = True
            self.level = random.randint(1,10)
            self.setLoot(self.level)

        else:
            self.hp = player_level + random.randint(15,25)
            self.strength = player_level + random.randint(5,10)
            # self.armor = random.randint(2,8)
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
        print Fore.GREEN+str(self.getShortName())+Fore.WHITE+" strikes and hits you in the face.\n"
        return player.takeDamage(damage,room.monster)

    def attack(self,room,player):
        damage = player.getStrength()+random.randint(0,3)
        if (self.hp - damage <= 0):
            room.killMonster()
            player.facesMonster = False

            if self.hasLoot:
                return self.handler.strMonster("killedLoot",self,player)+"\n"+player.addItem(self.getLoot())
            else:
                return self.handler.strMonster("killed",self,player)

        else:
            self.takeDamage(damage)
            return "You attack" + Fore.GREEN+" %s "%(self.getShortName())+ Fore.WHITE +\
             "and you deal" +Fore.RED+" %s "%(damage)+Fore.WHITE+"damage.\n"+\
             "The Monster's Health is now at "+Fore.GREEN +str(self.getHP())+Fore.WHITE

    def flee(self, room, player):
            player.facesMonster = False
            damage = random.randint(1,15)
            string = Fore.RED +"%s "%(self.getShortName())+ Fore.WHITE+"laughs manically as you try to flee from it\n"
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
                    return Fore.WHITE, "You took {0} damage, you are now dead".format(damage)
                else:
                    player.takeDamage(damage,room.monster)
                    return Fore.WHITE +"\nA wild" +Fore.GREEN+ " %s "%(self.getFullName()) + \
                    Fore.WHITE+ "appears!\n%s attacks and you take"%(self.getShortName()) + \
                    Fore.RED + " %s " % (damage) + Fore.WHITE +"damage.\n" + \
                    Fore.CYAN +"\n%s"%(player.name)+ Fore.WHITE+", your HP is now at "+ Fore.CYAN + str(player.getHP()) + Fore.WHITE +"\n"
