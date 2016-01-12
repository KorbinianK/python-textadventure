from settings import Settings
from player import Player
from colorama import init, Fore, Back, Style

from items import Items
import random

class Actions():
    def __init__(self, action, player, monster):

        self.action = action
        self.player = player
        self.monster = monster
        #self.items = items


    def __repr__(self):
        #items = Items()

        ##
        ## Summons a monster
        ##
        if(self.action == "monster" ):
            if not self.monster.killed and self.player.facesMonster:
                damage = random.randint(1,15)
                self.player.takeDamage(damage)
                return "You already face %s, and it attacks you. You take"%(self.monster.getShortName()) + \
                Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n" + \
                "%s, your HP is now at "%(self.player.name)+ Fore.CYAN + str(self.player.getHP()) + Style.RESET_ALL +"\n"
            else:
                self.player.facesMonster = True
                damage = random.randint(1,15)
                if(int(self.player.getHP()) - damage < 0):
                    self.player.takeDamage(damage)
                    return Style.RESET_ALL, "You took {0} damage, you are now dead".format(damage)

                else:
                    self.player.takeDamage(damage)
                    return Style.RESET_ALL +"A wild" +Fore.GREEN+ " %s "%(self.monster.getFullName()) + \
                    Style.RESET_ALL+ "appears!\n%s attacks and you take"%(self.monster.getShortName()) + \
                    Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n" + \
                    Fore.CYAN +"%s"%(self.player.name)+ Style.RESET_ALL+", your HP is now at "+ Fore.CYAN + str(self.player.getHP()) + Style.RESET_ALL +"\n"

        ##
        ## Attacks the monster
        ##
        elif(self.action == "attack"):
            if not self.monster.killed and self.player.facesMonster:
                damage = self.player.strength + random.randint(0,2)
                if (self.monster.getHP() - damage <= 0):
                    self.monster.killed = True
                    self.player.facesMonster = False
                    if self.monster.hasLoot:
                        self.player.addItem(self.monster.getLoot())
                        return "You killed %s"%(self.monster.getShortName())+" and it drops some Loot! " +\
                                "Oh look, it's"+Fore.YELLOW+" %s!"%(self.monster.getLoot().name+Style.RESET_ALL)
                    else:
                        return "You killed %s"%(self.monster.getShortName())
                else:
                    self.monster.takeDamage(damage)
                    return "You attack" + Fore.GREEN+" %s "%(self.monster.getShortName())+ Style.RESET_ALL +\
                     "and you deal" +Fore.RED+" %s "%(damage)+Style.RESET_ALL+"damage.\n"+\
                     "The Monster's Health is now at "+Fore.GREEN +str(self.monster.getHP())+Style.RESET_ALL
            else:
                return "You shake your fists and try to attack your shadows"

        ##
        ## Flees from a monster
        ##
        elif(self.action == "flee"):

            if(self.player.facesMonster):
                self.player.facesMonster = False
                damage = random.randint(1,15)
                string = Fore.RED +"%s "%(self.monster.getShortName())+ Style.RESET_ALL+"laughs manically as you try to flee from it\n"

                if damage < 5:
                    return string +"You barely manage, stumbling through the darkness \n" + \
                     "You take"+Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n"
                else:
                    return string +"As you run through the darkness you fall and hit your head on something. \n" + \
                     "You take"+Fore.RED + " %s " % (damage) + Style.RESET_ALL +"damage.\n"
                return
            else:
                return "'Coward! You stay exactly where you are!', shouts a voice and you tremble at it's power over you."


        ##
        ## Displays the items the player has
        ##

        elif(self.action == "inventory"):
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
            return Style.RESET_ALL +"Sorry, You cannot" + " '%s'.\n"%(self.action)+ \
            "Type" +Fore.CYAN+" help "+ Style.RESET_ALL+"to view currently available commands."



    # {def playerTakeDamage(self,action_input):
    # # Deals 1 damage to the player
    #         if action_input == "take damage":
    #             player.takeDamage(1)
    #             print(Style.RESET_ALL)
    #             print("\nYou slap yourself in the face \n"+"Your HP is now at " + Fore.RED + str(player.getHP()) +"\n"  )
    #             print(Style.RESET_ALL)
    #
    # def playerGetHP(self,action_input):
    # # Returns the current players HP
    #         if action_input == "hp":
    #             print(Style.RESET_ALL)
    #             print str(player.getHP())
    #
    # def playerMonster(self,action_input):
    # # The player gets attacked by a random "monster"
    #         if action_input == "monster":
    #             damage = random.randint(1,15)
    #             if(int(player.getHP()) - damage < 0):
    #                 print(Style.RESET_ALL)
    #                 print "You took %s damage, you are now dead" % (damage)
    #                 player.takeDamage(damage)
    #             else:
    #                 player.takeDamage(damage)
    #                 print(Style.RESET_ALL)
    #                 print ("A wild" +Fore.GREEN+ " %s "%(monster.getFullName())+ (Style.RESET_ALL)+ "appears!\n%s attacks and you take"%(monster.getShortName()) + Fore.RED + " %s " % (damage) + (Style.RESET_ALL) +"damage" )
    #                 print ("Your HP is now at "+ Fore.RED + str(player.getHP()) + (Style.RESET_ALL)+"\n")
    #
    # def playerShort(self,action_input):
    # # Test for short name generator
    #         if action_input == "short":
    #             print(Style.RESET_ALL)
    #             print ("You get hit by %s's attack and take"%(monster.getShortName()) + Fore.RED + " %s " % (1) + (Style.RESET_ALL) +"damage" )
    # def playerSettings(self,action_input):
    # # Returns difficulty
    #         if action_input == "settings":
    #             print(Style.RESET_ALL)
    #             print difficulty}
