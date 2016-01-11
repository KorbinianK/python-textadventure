from randommonstername import RandomMonsterName
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from colorama import init, Fore, Back, Style
import random

init()
def __init__(self):
    self.settings = Settings()
    self.difficulty = settings.difficulty

def play():
    print ("What is your name?\n")
    name_input = raw_input ('>: ')
    player = Player()
    player.name = name_input
    monster = Monster()
    monster.hasLoot = True


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
        response =  actions(action_input,player,monster)
        if player.condition is "normal":
            print response
        elif player.condition is "poisoned":
            #Do stuff with "response"
            print response

if __name__ == "__main__":
    play()
