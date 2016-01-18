from settings import Settings
from colorama import init, Fore, Back, Style
import time
import random,re

init()

class Actions():
    def __init__(self, action, player, room):

        self.action = action
        self.player = player
        self.room = room
        self.monster = room.monster
        self.chest = room.chest

    def __repr__(self):

        ##
        ## Summons a monster
        ##
        if(self.action.lower()== "monster" ):
            if self.room.hasMonster:
                return self.room.monster.spawn(self.room,self.player)
            else:
                return "The room is empty... like your soul. Do you want to"+Fore.CYAN+" continue"+Fore.WHITE +" or"+Fore.CYAN+" look around"+Fore.WHITE +"?"


        ##
        ## Equips an item
        ##

        elif("equip" in self.action.lower()):
            slot = int(re.search(r'\d+', self.action.lower()).group())-1

            if len(self.player.inventory) > 0 and slot is not None:
                return self.player.equipItem(slot)
            else:
                return "nope"

        ##
        ## Attacks the monster
        ##
        elif(self.action.lower()== "attack"):

            if not self.monster.killed and self.player.facesMonster:

                return self.room.attackMonster(self.player)
            else:
                return "You shake your fists and try to attack your shadows"

        ##
        ## Flees from a monster
        ##
        elif(self.action.lower()== "flee"):

            time.sleep(2)
            if(self.player.facesMonster):
                return self.room.monster.flee(self.room, self.player)
            else:
                return "'Coward! You stay exactly where you are!', shouts a voice and you tremble at it's power over you."

        ##
        ## Goes to next room, if possible
        ##

        elif(self.action.lower()== "continue"):

            if self.room.isDone:
                time.sleep(2)
                return "You progress to the next room"
            else:
                return "nope"

        ##
        ## Tells the player what the room has inside
        ##

        elif(self.action.lower()== "look around"):
            self.room.inspectRoom()
            if self.room.hasChest and not self.room.chest.opened:
                time.sleep(2)
                return "You see a"+Fore.YELLOW + " closed Chest "+Fore.WHITE+"in one corner of the room."
            elif self.room.hasChest and self.room.chest.opened:
                return "There seems to be only an open Chest in this room."
            time.sleep(2)
            return "You looked around. Good job."

        ##
        ## Let's the player open a chest, if he has inspected the room already
        ##
        elif(self.action.lower()== "open chest"):
            if self.room.inspected:
                if self.room.hasChest and not self.room.chest.opened:
                    return self.room.openChest()
                elif self.room.chest.opened:
                    return "Nice try... How about this instead? " + self.player.takeDamage(1)
            else:
                return "You seem to imagine things in the darkness. Maybe"+Fore.CYAN+" look around "+Fore.WHITE+"first."

        ##
        ## Displays the items the player has
        ##

        elif(self.action.lower()== "inventory"):
            if self.player.hasItems:
                return self.player.printInventory()
            else:
                time.sleep(2)
                return "You find some lint in your pockets, it looks pretty useless..."



        ##
        ## Just for debugging
        ##

        elif self.action == "p":
            return str(self.player.getStrength())

        elif(self.action == "cheat"):

            self.player.strength = 100
            self.player.name ="Lazy Cheater"
            return "You cheater! From now on we will refer to you as"+Fore.CYAN+" %s"%(self.player.name)+Fore.WHITE

        ##
        ## Displays available commands
        ##

        elif(self.action.lower() =="help"):
            return Back.WHITE + Fore.BLACK +"[monster] [attack] [inventory] [flee] [info] [help]" + Fore.WHITE
        ##
        ## Message if invalid command was used
        ##
        else:
            string = "Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
            "Type" +Fore.CYAN+" help "+ Fore.WHITE+"to view currently available commands."
            return string
