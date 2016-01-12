from randommonstername import RandomMonsterName
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from room import Room
from colorama import init, Fore, Back, Style
import random

init()

def play():
    settings = Settings()

    difficulty = settings.difficulty

    print ("What is your name?\n")
    name_input = raw_input ('>: ')
    player = Player()
    player.name = name_input
    room = Room(difficulty,player)
    monster = Monster()
    #hp,strength,armor,hasLoot,level
    if difficulty == "easy":
        monster.setup(1,player.level)
    else:
        monster.setup(2,player.level)
    # monster.setup(10,5,5,True,5)

#
# Asks for the player Name
#
    print (Style.RESET_ALL + "Hello"+Fore.CYAN + " %s"%(player.name) + Style.RESET_ALL +"!\n")
    print ("Welcome to our world of pain and suffering!\n")


#
# Game Loop start
#
    while player.is_alive() and not player.victory:

        print("What do you want to do?\n")

    #
    # Asks the player for some Input commands
    #
        action_input = raw_input(Fore.CYAN + '>: ')

        print Style.RESET_ALL
        if monster.killed:
            monster = Monster()
            if difficulty == "easy":
                monster.setup(1,player.level)
            else:
                monster.setup(2,player.level)

        response =  actions(action_input,player,monster)
        if player.condition is "normal":
            print response
        elif player.condition is "poisoned":
            #Do stuff with "response"
            print response

if __name__ == "__main__":
    play()
