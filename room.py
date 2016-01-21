from monster import Monster
from chest import Chest
import random, time,sys
from random import uniform
from colorama import init, Fore, Back, Style
from stringhandler import Stringhandler

class Room(object):

    def __init__(self,difficulty,player):

        self.hasMonster = False
        self.hasChest = False
        self.isDone = False
        self.difficulty = difficulty
        self.player = player
        self.chest = Chest(self.player)
        self.monster = Monster()
        self.inspected = False
        self.handler = Stringhandler()
        #self.name = "default"+str(random.randint(0,10))
        #self.newRoom()

    # Sets up a new Room and displays some "Intro Text"
    def newRoom(self):
        self.isDone = False

        string = "\n\n#######################################"+"\n\n"+\
        self.handler.strRoom("opening",self)+"\n\n"+\
        "#######################################"+"\n\n"
        for char in string:
            time.sleep(uniform(0.05, 0.01))
            sys.stdout.write('\033[35m'+char)
            sys.stdout.flush()

        print Fore.WHITE
        # Decides whether the room gets a monster or a chest
        rnd = random.randint(0,10)
        if rnd > 1:
            self.hasMonster = True
        else:
            self.hasChest = True

        # Setup monster
        if self.hasMonster:
            if self.difficulty == "easy":
                self.monster.setup(1,self.player.level)
            else:
                self.monster.setup(2,self.player.level)


        # Setup chest
        elif self.hasChest:

            if self.difficulty == "easy":
                self.chest.level = random.randint(1,10)
            else:
                self.chest.level = random.randint(1,10)
        else:
            self.finish()

    def getRoom(self,difficulty,player):

        return Room(difficulty,player)

    # If the player has used "look around" the room should be set to inspected
    # room.inspectRoom()
    def inspectRoom(self):

        self.inspected = True

    # Kills the monster in this Room, required for the player to be able to continue -> Room set to "Done"
    def killMonster(self):

        self.monster.kill()
        self.player.lvlUp()
        self.finish()


    def attackMonster(self,player):
        room  = self
        return self.monster.attack(room,player)

    # Opens the chest, required for the player to be able to continue -> Room set to "Done"
    def openChest(self):
        self.finish()
        return self.chest.open(self.player)

    def is_done(self):
        return self.isDone

    def finish(self):

        self.isDone = True
        if self.hasChest:
            self.chest.is_opened = True
