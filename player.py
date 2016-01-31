from colorama import init, Fore, Back, Style
from settings import Settings
from weapon import Weapon
from potion import Potion
import time,sys,random,re
from random import uniform
from stringhandler import Stringhandler
from bosslist import ByteBoss,HipsterBoss

class Player(object):

    def __init__(self):
    	self.name = "player"
        self.hp = 100
        self.facesMonster = False
        self.facesBoss = False
        self.victory = False
        self.condition = "normal"
        self.previous = "normal"
        self.strength = 5
        self.level = 1
        self.inventory =[]
        self.is_in_room = False
        self.equipped = []
        self.triedWalk = False
        self.alive = True
        self.settings = Settings()
        self.handler = Stringhandler()

    def is_alive(self):
        return self.hp > 0

    def is_in_room(self):
        return self.is_in_room

    def getCondition(self):
        return self.condition

    def setCondition(self,condition):
        self.condition = condition

    def wins(self):
        self.facesBoss = False
        self.facesMonster = False
        self.victory = True

    def takeDamage(self, damage, monster):
        self.hp -= damage
        rnd = random.randint(0,20)
        if rnd < 3:
            self.previous = self.condition
            self.condition = "poisoned"
        elif rnd is 10 or 15 or 20:
            if self.condition == "poisoned":
                self.condition = "normal"
                self.previous = "poisoned"
        else:
            self.previous = self.condition
        if self.hp > 0:
            if self.facesBoss:

                if isinstance(monster,ByteBoss) or isinstance(monster,HipsterBoss):
                    if isinstance(monster,ByteBoss):
                        return self.handler.strBoss("bAttack",self,damage)+"\n"+self.handler.strPlayer("condition",self)+self.handler.strPlayerDamage("hp",self,monster,damage)+"\n"
                    elif isinstance(monster,HipsterBoss):
                        return self.handler.strBoss("hAttack",self,damage)+"\n"+self.handler.strPlayer("condition",self)+self.handler.strPlayerDamage("hp",self,monster,damage)+"\n"
                    else:
                        return "Uh oh, not good."
            else:
                return "\n"+self.handler.strPlayerDamage("takeDamage",self,monster,damage)+"\n"+self.handler.strPlayer("condition",self)+self.handler.strPlayerDamage("hp",self,monster,damage)+"\n"
        else:
            return self.die(monster)

    def lvlUp(self):
        self.level +=1
        print self.handler.strPlayer("lvl",self)

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.condition = condition
    def getPrevious(self):
        return self.previous

    def is_facing_Monster(self):
        return self.facesMonster

    def facing_Monster(self, status):
        self.facesMonster = status

    def addItem(self, item):
        self.inventory.append(item)
        self.hasItems = True
        if isinstance(item,Weapon):
            print "\n"+self.handler.strPlayerItem("newItem", self, item)
            return self.equipItem(len(self.inventory)-1,item)

    def equipItem(self,pos,item):
        slot = pos
        if int(slot) >= len(self.inventory):
            string = "Sorry Dave, I'm afraid I can't let you do that."
        else:
            self.equipped = self.inventory[slot]
            # return "\n"+self.handler.strPlayerItem("newItem", self, item)
            if isinstance(item,Weapon):
                self.strength = 1
                self.strength += self.equipped.damage
            # print "\nYou equipped "+Fore.YELLOW + item.name+Fore.WHITE
            string = self.handler.strPlayerItem("equipItem", self, item)
        return string

    def heal(self):
        if isinstance(self.equipped,Potion):
            if not self.equipped.isEmpty:
                self.equipped.drink()
                heal = int(self.hp*self.equipped.strength)
                if self.hp + heal <= 100:
                    self.hp += heal
                    return "\n"+self.handler.strPlayer("heal", self)
                else:
                    self.hp = 100
                    return "\n"+self.handler.strPlayer("healFull", self)
            else:
                return "\n"+self.handler.strPlayer("emptyPot", self)

        elif isinstance(self.equipped,list):
            return "\n"+self.handler.strPlayer("drinkAir", self)
        else:
            return self.handler.strPlayerItem("drinkItem", self,self.equipped)

    def die(self, monster):
        stringtwo = ""
        if monster is not None:
            string = self.handler.strPlayer("dies",self)
        else:
            string = self.handler.strPlayer("dies",self)+"\n"

        if "SHAKESPEAR" in string:
            string =string.replace("SHAKESPEAR ","")
            stringtwo = "to die, to sleep..."
        elif "FORGET" in string:
            string = string.replace("FORGET ","")
            stringtwo = "\nDo not forget me..."
        elif "FIREFLY" in string:
            string = string.replace("FIREFLY ","")
            stringtwo = "\nCurse your sudden but inevitable betrayal..."

        for char in string:
            time.sleep(uniform(0.05, 0.1))
            sys.stdout.write('\033[36m'+char)
            sys.stdout.flush()

        for char in stringtwo:
            time.sleep(uniform(0.1, 0.6))
            sys.stdout.write('\033[36m'+char)
            sys.stdout.flush()
        self.alive = False
        return Fore.WHITE+"\n\n\nYou are dead.\n\n"
        #"+Fore.CYAN+"restart "+Fore.WHITE+"or"+Fore.CYAN+" exit?"

    def getStrength(self):
        return self.strength

    def printInventory(self):
        string = "You own: "
        for index,item in enumerate(self.inventory, start=1):
             string = string+Fore.YELLOW+item.name+Fore.WHITE+"[" + str(index) +"], "
        string = string + "\nType"+Fore.CYAN +" equip 1 "+Fore.WHITE+"to equip the first item form the list."
        return self.handler.modify(string, self)
