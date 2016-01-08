
from player import Player

def play():

    player = Player()

    while player.is_alive() and not player.victory:

        if player.is_alive() and not player.victory:
            print("What do you want to do?\n")
            action_input = raw_input('>: ')
            if action_input == "take damage":
                player.takeDamage(15)
                
if __name__ == "__main__":
    play()
