from settings import Settings
from colorama import init, Fore, Back, Style
from stringhandler import Stringhandler
import time
import random,re,sys

init()

class Actions():
    def __init__(self, action, player, room):

        self.action = action
        self.player = player
        self.room = room
        self.monster = room.monster
        self.chest = room.chest
        self.handler = Stringhandler()

    def __repr__(self):

        if self.player.alive:

            ##
            ## Continues
            ##
            if "go" in self.action.lower() or "walk" in self.action.lower() or "continue" in self.action.lower():
                text = self.handler.strActions("moving",self.player,self.room)
                for x in range (0,5):
                    b = text + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.4)

                if self.room.hasMonster:
                    if not self.room.monster.killed:
                        self.player.triedWalk = True
                        damage = self.room.monster.calcDamage()
                        return self.room.monster.attackPlayer(self.room,self.player,damage)
                        # response = "a"
                    else:
                        return self.handler.strActions("nextRoomMonster",self.player,self.room) +\
                         "\n"+self.handler.strActions("nextRoom",self.player,self.room)
                        # response = "b"
                elif not self.room.isDone:
                    return self.handler.strActions("moveChest",self.player,self.room)
                else:
                    return self.handler.strActions("nextRoom",self.player,self.room)
            elif "die" == self.action.lower():
                return self.player.die(self.room.monster)

            ##
            ## Equips an item
            ##
            elif "equip" in self.action.lower():
                if bool(re.search(r'\d', self.action.lower())):
                    slot = int(re.search(r'\d+', self.action.lower()).group())-1
                    if slot < len(self.player.inventory):
                        return self.player.equipItem(slot,self.player.inventory[slot])
                    else:
                        return "You only have "+Fore.GREEN+str(len(self.player.inventory))+Fore.WHITE+" item(s) in your"+Fore.CYAN+" inventory" +Fore.WHITE+"."
                else:
                    return "You can't do that.\nUse "+Fore.CYAN+"equip 1" +Fore.WHITE+" to equip the first item of your"+Fore.CYAN+" inventory "+Fore.WHITE+"."

            ##
            ## Drinks a potion
            ##

            elif "drink" in self.action.lower():

                return self.player.heal()


            ##
            ## Attacks the monster
            ##
            elif(self.action.lower()== "attack"):

                if not self.monster.killed and self.player.facesMonster:

                    return self.room.attackMonster(self.player)
                elif self.player.facesBoss:
                    boss = self.room.getBoss()
                    return boss.attackFromPlayer(self.player)
                else:
                    return self.handler.strActions("attackNoMonster",self.player,self.room)

            ##
            ## Flees from a monster
            ##
            elif(self.action.lower()== "flee"):

                time.sleep(2)
                if(self.player.facesMonster):
                    response = self.room.monster.flee(self.room, self.player)
                else:
                    response = self.handler.strActions("fleeNoMonster",self.player,self.room)
                text = self.handler.strActions("fleeing",self.player,self.room)
                for x in range (0,5):
                    b = text + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.3)
                return response

            ##
            ## Tells the player what the room has inside
            ##

            elif(self.action.lower()== "look around"):
                self.room.inspectRoom()
                if self.room.hasChest and not self.room.chest.opened:
                    if self.room.inspected:
                        response = self.handler.strActions("lookClosedChest",self.player,self.room)
                    else:
                        response = self.handler.strActions("openChestNoLook",self.player,self.room)
                elif self.room.hasChest and self.room.chest.opened:
                    response = self.handler.strActions("lookOpenChest",self.player,self.room)
                else:
                    response = self.handler.strActions("lookNothing",self.player,self.room)
                text = self.handler.strActions("looking",self.player,self.room)
                for x in range (0,5):
                    b = text + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.4)

                return "\n"+response

            ##
            ## Let's the player open a chest, if he has inspected the room already
            ##
            elif(self.action.lower()== "open chest"):
                if self.room.inspected:
                    if self.room.hasChest and not self.room.chest.opened:
                        response = self.handler.strActions("chestOpens",self.player,self.room) +"\n"+ str(self.room.openChest())
                    elif self.room.chest.opened:
                        return "\n"+self.handler.strActions("chestOpenAgain",self.player,self.room)
                else:
                    response = self.handler.strActions("openChestNoLook",self.player,self.room)
                text = self.handler.strActions("tryOpenChest",self.player,self.room)
                for x in range (0,5):
                    b = text + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.2)
                return "\n"+response

            ##
            ## Displays the items the player has
            ##

            elif(self.action.lower()== "inventory"):
                if self.player.hasItems:
                    response = self.player.printInventory()
                else:
                    response = "You find some lint in your pockets, it looks pretty useless..."
                text = self.handler.strActions("searchingInventory",self.player,self.room)
                for x in range (0,5):
                    b = text + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.5)
                return "\n\n"+response

            ##
            ## Just for debugging
            ##

            elif self.action == "info":
                return "Strength: "+str(self.player.getStrength()) + \
                "\nHP: "+str(self.player.getHP()) + \
                "\nLvl: "+str(self.player.level)+\
                "\nVictory: "+str(self.player.victory)+\
                "\nCondition: "+str(self.player.getCondition())+\
                "\nPrevCond: "+str(self.player.getPrevious())

            elif(self.action == "cheat"):
                self.player.lvlUp()
                self.player.strength = 10
                self.player.name ="Lazy Cheater"
                return "You cheater! From now on we will refer to you as"+Fore.CYAN+" %s"%(self.player.name)+Fore.WHITE

            elif(self.action == "p"):
                self.player.condition = "poisoned"
                return "poisoned"
            ##
            ## Displays available commands
            ##

            elif(self.action.lower() =="help"):
                return Back.WHITE + Fore.BLACK +"[attack] [inventory] [flee] [info] [continue] [equip x] [inventory] [look around] [open chest]" +Back.BLACK + Style.RESET_ALL + Style.BRIGHT

            ##
            ## Message if invalid command was used
            ##
            else:

                string = "Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
                "Type" +Fore.CYAN+" help "+ Fore.WHITE+"to view currently available commands."
                return string
        ##
        ## Message if invalid command was used
        ##
        else:

            string = "Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
            "Type" +Fore.CYAN+" help "+ Fore.WHITE+"to view currently available commands."
            return string
