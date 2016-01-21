from settings import Settings
from colorama import init, Fore, Back, Style
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

    def __repr__(self):

        if self.player.alive:
            ##
            ## Summons a monster
            ##
            if self.action.lower()== "monster":
                if self.room.hasMonster:
                    return self.room.monster.spawn(self.room,self.player)
                else:
                    return "The room is empty... like your soul. Do you want to"+Fore.CYAN+" continue"+Fore.WHITE +" or"+Fore.CYAN+" look around"+Fore.WHITE +"?"


            ##
            ## Continues
            ##
            elif "go" in self.action.lower() or "walk" in self.action.lower() or "continue" in self.action.lower():
                for x in range (0,5):
                    b = "Moving towards the door" + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.4)

                if self.room.hasMonster:
                    if not self.room.monster.killed:
                        self.player.triedWalk = True
                        return self.room.monster.attackPlayer(self.room,self.player)
                        # response = "a"
                    else:
                        return "You almost stumble over the carcass of "+str(self.room.monster.getShortName()) + "\nYou walk through the door into the next room"
                        # response = "b"
                elif not self.room.isDone:
                    return "Carefully you walk through the darkness.\nThen you hit your knee on something... Maybe you should"+Fore.CYAN+" look around "+Fore.WHITE+"first?"
                else:
                    return "You walk through the door into the next room"

            ##
            ## Equips an item
            ##

            elif "equip" in self.action.lower():
                slot = int(re.search(r'\d+', self.action.lower()).group())-1

                if len(self.player.inventory) > 0 and slot is not None:
                    return self.player.equipItem(slot,self.player.inventory[slot])
                else:
                    return "nope"

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
                else:
                    return "You shake your fists and try to attack your shadows"

            ##
            ## Flees from a monster
            ##
            elif(self.action.lower()== "flee"):

                time.sleep(2)
                if(self.player.facesMonster):
                    response = self.room.monster.flee(self.room, self.player)
                else:
                    response = "'Coward! You stay exactly where you are!', shouts a voice and you tremble at it's power over you."
                for x in range (0,5):
                    b = "Trying to flee" + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.3)
                return response

            ##
            ## Tells the player what the room has inside
            ##

            elif(self.action.lower()== "look around"):
                self.room.inspectRoom()
                if self.room.hasChest and not self.room.chest.opened:
                    response = "You see a"+Fore.YELLOW + " closed Chest "+Fore.WHITE+"in one corner of the room."
                elif self.room.hasChest and self.room.chest.opened:
                    response = "There seems to be only an open Chest in this room."
                else:
                    response = "You looked around. Good job."
                for x in range (0,5):
                    b = "Looking around" + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.4)

                return response

            ##
            ## Let's the player open a chest, if he has inspected the room already
            ##
            elif(self.action.lower()== "open chest"):
                if self.room.inspected:
                    if self.room.hasChest and not self.room.chest.opened:
                        response = "The chest opens with a loud squeaky noise\n" + str(self.room.openChest())
                    elif self.room.chest.opened:
                        response = "Nice try... How about this instead? "
                else:
                    response = "You seem to imagine things in the darkness. Maybe"+Fore.CYAN+" look around "+Fore.WHITE+"first."
                for x in range (0,5):
                    b = "You try to open the chest" + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.2)
                return response

            ##
            ## Displays the items the player has
            ##

            elif(self.action.lower()== "inventory"):
                if self.player.hasItems:
                    response = self.player.printInventory()
                else:
                    response = "You find some lint in your pockets, it looks pretty useless..."
                for x in range (0,5):
                    b = "You are searching your pockets" + "." * x
                    sys.stdout.write('\r'+b)
                    time.sleep(0.5)
                return "\n\n"+response



            ##
            ## Just for debugging
            ##

            elif self.action == "info":
                return "Strengrn: "+str(self.player.getStrength()) + \
                "\nHP: "+str(self.player.getHP()) + \
                "\nLvl: "+str(self.player.level)+\
                "\nVictory: "+str(self.player.victory)

            elif(self.action == "cheat"):
                print self.player.lvlUp()
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
        ##
        ## Message if invalid command was used
        ##
        else:

            string = "Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
            "Type" +Fore.CYAN+" help "+ Fore.WHITE+"to view currently available commands."
            return string
