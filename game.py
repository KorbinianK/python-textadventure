from randommonstername import RandomMonsterName
from player import Player
from colorama import init, Fore, Back, Style
import random

def play():

    player = Player()
    monstername = RandomMonsterName()

    while player.is_alive() and not player.victory:

        print("What do you want to do?\n")

# Asks the player for some Input
        action_input = raw_input('>: ')

# Deals 1 damage to the player
        if action_input == "take damage":
            player.takeDamage(1)
            print("\nYou slap yourself in the face \n"+"Your HP is now at " + Fore.RED + str(player.getHP()) +"\n"  )
            print(Style.RESET_ALL)

# Returns the current players HP
        if action_input == "hp":
            print str(player.getHP())

# The player gets attacked by a random "monster"
        if action_input == "monster":
            damage = random.randint(1,15)
            if(int(player.getHP()) - damage < 0):
                print "You took %s damage, you are now dead" % (damage)
                player.takeDamage(damage)
            else:
                player.takeDamage(damage)
                print ("You get hit by %s's attack and take"%(monstername.getFullName()) + Fore.RED + " %s " % (damage) + (Style.RESET_ALL) +"damage" )
                print ("Your HP is now at "+ Fore.RED + str(player.getHP()) + (Style.RESET_ALL)+"\n")

# Test for short name generator
        if action_input == "short":
            print ("You get hit by %s's attack and take"%(monstername.getOnlyName()) + Fore.RED + " %s " % (1) + (Style.RESET_ALL) +"damage" )
            

if __name__ == "__main__":
    play()
