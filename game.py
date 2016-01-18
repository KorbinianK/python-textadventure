from randommonstername import RandomMonsterName
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from room import Room
from items import Items
from colorama import init, Fore, Back, Style
import random, time, re, sys


init(autoreset=True)

def play():
    text_file = open("Output.txt", "w")
    settings = Settings()
    difficulty = settings.difficulty
    player = Player()
    item = Items()

    print ("What is your name?\n")
    name_input = raw_input ('>: ')
    player.name = name_input
#
# Asks for the player Name
#

    print '{:^90}'.format("Hello"+Fore.CYAN + " %s"%(player.name) + Style.RESET_ALL +"!")
    print '{:^80}'.format("Welcome to our world of pain and suffering!")

    if not player.is_in_room:
        player.addItem(item.newPotion(0.2,5))
        room = Room(difficulty,player)
        room.newRoom()
        player.is_in_room = True


#
# Game Loop start
#
    while player.is_alive() and not player.victory:


        print ("\nWhat do you want to do?\n")

    #
    # Asks the player for some Input commands
    #
        action_input = raw_input(Fore.CYAN + player.name+ '>: ')
        print Style.RESET_ALL
        if room.is_done() and action_input.lower() == "continue":
            response = actions(action_input,player,room)
            print response
            room = room.getRoom(difficulty,player)
            room.newRoom()
        elif action_input.lower() == "restart":
            print Back.WHITE+"                  "+Fore.BLACK+"Game restarted"+ Back.WHITE +Fore.RED+"                  \n"+Style.RESET_ALL
            text_file.close()
            play()
        elif action_input.lower() == "exit":
            print Back.RED+"                  "+Fore.WHITE+"Game exited"+ Back.RED +"                  \n"+Style.RESET_ALL
            text_file.close()
            break;
        else:
            # The magic happens here:
            response = actions(action_input,player,room)
            if player.condition is "normal":

                string = str(response)
                text_file.write(string)
                print string

            elif player.condition is "poisoned":
                #Do stuff with "response"
                string = re.sub(r'(\x1b[^m]*m)',r'\1', str(response)[::-1])
                print string

if __name__ == "__main__":
    play()
