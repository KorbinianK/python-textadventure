from randommonstername import RandomMonsterName
from player import Player
from colorama import init, Fore, Back, Style
import random

def play():

    player = Player()
    monstername = RandomMonsterName()

    while player.is_alive() and not player.victory:

        if player.is_alive() and not player.victory:
            print("What do you want to do?\n")

            action_input = raw_input('>: ')

            if action_input == "take damage":
                player.takeDamage(1)

            if action_input == "hp":
                print player.returnHP()

            if action_input == "monster":
                damage = random.randint(1,5)
                player.takeDamage(damage)
                print ("You get hit by %s's attack and lose"%(monstername.getName()) + Fore.RED + " %s " % (damage) + (Style.RESET_ALL) +"health" )
                print ("Your HP is now at "+player.returnHP())


if __name__ == "__main__":
    play()
