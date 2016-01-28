from randommonstername import RandomMonsterName
from stringhandler import Stringhandler
from player import Player
from actions import Actions as actions
from settings import Settings
from monster import Monster
from room import Room
from items import Items
from colorama import init, Fore, Back, Style
import random, time, re, sys
from random import uniform

# init()

def play():

    handler = Stringhandler()
    settings = Settings()
    goal = settings.getGoal()
    difficulty = settings.difficulty
    player = Player()
    item = Items()


    intro = handler.strIntro()
    for char in "\n"+intro+"\n":
        time.sleep(uniform(0.05, 0.1))
        sys.stdout.write('\033[35m'+'\033[1m'+char)
        sys.stdout.flush()
    name_input = raw_input (Fore.CYAN +'\n>: ')
    player.name = name_input
#
# Asks for the player Name
#
    print Style.BRIGHT + Fore.WHITE
    greeting = handler.strGreeting(player)

    string = re.sub(r'(\x1b[^m]*m)',"", str(greeting+"\n"))

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
        chest = room.newRoom()
        string = room.monster.spawn(room,player)
        if room.hasMonster:
            player.is_in_room = True
            print str(string)
        else:
            print chest


#
# Game Loop start
#
    while player.is_alive():

        if player.victory:
            print "Do you want to"+Fore.CYAN+" restart"+Fore.WHITE+" or"+Fore.CYAN+" exit"+Fore.WHITE+"?"
            end_input = raw_input(Fore.CYAN +"\n"+ player.name+ '>: ')
            if end_input.lower() == "restart":
                # player.alive = True
                print handler.strBasic("restart")
                play()
            elif end_input.lower() == "exit":
                print handler.strBasic("exit")
                break;
        else:
            #print ("\nWhat do you want to do?\n")
            action_input = raw_input(Fore.CYAN +"\n"+ player.name+ '>: ')
            print Fore.WHITE
            if room.is_done() and ("go" in action_input.lower() or "walk" in action_input.lower() or "continue" in action_input.lower()):
                response = actions(action_input,player,room)
                print response
                room = room.getRoom(difficulty,player)
                chest = room.newRoom()
                string = room.monster.spawn(room,player)
                if room.hasMonster:
                    print str(string)
                else:
                    print chest

            elif action_input.lower() == "restart":
                player.alive = True
                print handler.strBasic("restart")
                play()
            elif action_input.lower() == "exit":
                print handler.strBasic("exit")
                break;

            else:
                # The magic happens here:
                time.sleep(0.5)
                # print player.condition
                print actions(action_input,player,room)



    if player.victory:
        print "Victory!"



if __name__ == "__main__":
    play()