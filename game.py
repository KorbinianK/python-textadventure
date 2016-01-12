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
    
#
# Asks for the player Name
#
    print Style.RESET_ALL
    print '{:^90}'.format("Hello"+Fore.CYAN + " %s"%(player.name) + Style.RESET_ALL +"!")
    print '{:^80}'.format("Welcome to our world of pain and suffering!")


#
# Game Loop start
#
    while player.is_alive() and not player.victory:

        if not player.is_in_room:
            room.newRoom()
            player.is_in_room = True

        print ("\nWhat do you want to do?\n")

    #
    # Asks the player for some Input commands
    #
        action_input = raw_input(Fore.CYAN + '>: ')

        print Style.RESET_ALL

        response = actions(action_input,player,room)
        if player.condition is "normal":
            print response
        elif player.condition is "poisoned":
            #Do stuff with "response"
            print response

if __name__ == "__main__":
    play()
