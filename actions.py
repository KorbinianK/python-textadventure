from settings import Settings
from player import Player
from colorama import init, Fore, Back, Style

from items import Items
import random

init(autoreset=True)

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
        if(self.action.lower() == "monster" ):
            if self.room.hasMonster:
                return self.room.monster.spawn(self.room,self.player)
            else:
                return "The room is empty... like your soul. Do you want to"+Fore.CYAN+" continue"+Style.RESET_ALL +" or"+Fore.CYAN+" look around"+Style.RESET_ALL +"?"

        ##
        ## Attacks the monster
        ##
        elif(self.action.lower() == "attack"):
            if not self.monster.killed and self.player.facesMonster:
                return self.room.monster.attack(self.room, self.player)
            else:
                return "You shake your fists and try to attack your shadows"

        ##
        ## Flees from a monster
        ##
        elif(self.action.lower() == "flee"):
            if(self.player.facesMonster):
                return self.room.monster.flee(self.room, self.player)
            else:
                return "'Coward! You stay exactly where you are!', shouts a voice and you tremble at it's power over you."

        ##
        ## Goes to next room, if possible
        ##

        elif(self.action.lower() == "continue"):
            return "nope"

        ##
        ## Tells the player what the room has inside
        ##

        elif(self.action.lower() == "look around"):
            self.room.inspectRoom()
            if self.room.hasChest and not self.room.chest.opened:
                return "You see a"+Fore.YELLOW + " closed Chest "+Style.RESET_ALL+"in one corner of the room."
            elif self.room.hasChest and self.room.chest.opened:
                return "There seems to be only an open Chest in this room."
            return "You look around. Good job."

        ##
        ## Let's the player open a chest, if he has inspected the room already
        ##
        elif(self.action.lower() == "open chest"):
            if self.room.inspected:
                if self.room.hasChest and not self.room.chest.is_opened():
                    if self.room.chest.hasLoot:
                        self.player.addItem(self.room.chest.open())
                        return "opened chest"
                    else:
                        return "You open the chest. It's empty."
                else:
                    return "Nice try... How about this instead? " + self.player.takeDamage(1)
            else:
                return "You seem to imagine things in the darkness. Maybe"+Fore.CYAN+" look around "+Style.RESET_ALL+"first."

        ##
        ## Displays the items the player has
        ##

        elif(self.action.lower() == "inventory"):
            if self.player.hasItems:
                return self.player.printInventory()
            else:
                return "You find some lint in your pockets, it looks pretty useless..."



        ##
        ## Just for debugging
        ##

        elif(self.action == "cheat"):

            self.player.strength = 100
            self.player.name ="Lazy Cheater"
            return "You cheater! From now on we will refer to you as"+Fore.CYAN+" %s"%(self.player.name)+Style.RESET_ALL

        ##
        ## Displays available commands
        ##

        elif(self.action =="help"):
            return Back.WHITE + Fore.BLACK +"[monster] [attack] [inventory] [flee] [info] [help]" + Style.RESET_ALL
        ##
        ## Message if invalid command was used
        ##
        else:
            string = Style.RESET_ALL +"Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
            "Type" +Fore.CYAN+" help "+ Style.RESET_ALL+"to view currently available commands."
            return string
