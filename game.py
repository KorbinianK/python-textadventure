from randommonstername import RandomMonsterName
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from room import Room
from items import Items
from colorama import init, Fore, Back, Style
import random, time, re, sys
from random import uniform

init()

def play():

    settings = Settings()
    difficulty = settings.difficulty
    player = Player()
    item = Items()

    for char in "\nHello there!\nHow should we call you?\n":
        time.sleep(uniform(0.05, 0.1))
        sys.stdout.write('\033[35m'+'\033[1m'+char)
        sys.stdout.flush()
    name_input = raw_input (Fore.CYAN +'\n>: ')
    player.name = name_input
#
# Asks for the player Name
#
    print Style.BRIGHT + Fore.WHITE
    string = re.sub(r'(\x1b[^m]*m)',r'\1', str("Hello %s"%(player.name)+"!\nWelcome to our world of pain and suffering!\n"))
    pos = string.find(player.name)
    for index, char in enumerate(string):
        time.sleep(uniform(0.05, 0.1))
        if index >= pos and index < pos+len(player.name):
            sys.stdout.write('\033[36m'+char)
        elif index == pos+len(player.name):
            sys.stdout.write('\033[37m'+char)
        else:
            sys.stdout.write('\033[37m'+char)
        sys.stdout.flush()

    if not player.is_in_room:
        player.addItem(item.newPotion(0.2,5))
        room = Room(difficulty,player)
        time.sleep(0.5)
        room.newRoom()
        string = room.monster.spawn(room,player)
        if room.hasMonster:
            print str(string)
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
        print Fore.WHITE
        if room.is_done() and ("go" in action_input.lower() or "walk" in action_input.lower() or "continue" in action_input.lower()):
            response = actions(action_input,player,room)
            print response
            room = room.getRoom(difficulty,player)
            room.newRoom()
            string = room.monster.spawn(room,player)
            if room.hasMonster:
                print str(string)
        elif action_input.lower() == "restart":
            print Back.WHITE+"                  "+Fore.BLACK+"Game restarted"+ Back.WHITE +Fore.RED+"                  \n"+Fore.WHITE

            play()
        elif action_input.lower() == "exit":
            print Back.RED+"                  "+Fore.WHITE+"Game exited"+ Back.RED +"                  \n"+Fore.WHITE

            break;

        else:
            # The magic happens here:
            response = actions(action_input,player,room)
            if player.condition is "normal":

                string = str(response)
                print string

            elif player.condition is "poisoned":
                #Do stuff with "response"
                string = re.sub(r'(\x1b[^m]*m)',r'\1', str(response)[::-1])
                print string

    if player.victory:
        print "Victory!"


if __name__ == "__main__":
    play()
