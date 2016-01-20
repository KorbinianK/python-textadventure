from colorama import init, Fore, Back, Style
import random


class Stringhandler(object):

    def __init__(self):

        self.strlist = []


    def strMonster(self,type,monster,player):
        name = str(Fore.GREEN+monster.getShortName()+ Fore.WHITE)
        item = str(Fore.YELLOW+monster.getLoot().name + Fore.WHITE)

        if type == "killedLoot":
            self.strlist.append("You killed "+ name  +" and it drops some Loot!")
            self.strlist.append(name+ ' is dead! Oh look something is on the ground.')
            self.strlist.append('The mighty oh glorious '+name+' left you something special after his death. Just take a moment and appreciate it.')
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)

        elif type == "killed":
            self.strlist.append("You killed "+ name+"!")
            self.strlist.append('You beat' +name+ 'into oblivion.')
            self.strlist.append(name+ ' is dead!')
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)

        elif type == "loot":
            self.strlist.append("Oh look, it's "+item+"!")
            self.strlist.append('Someone seems to favour you... A new '+item+'!')
            self.strlist.append('uuuuh, look what you found! You better keep that little precious '+item+", 'cause you will never know when you need it. *blink*")
            self.strlist.append("MY PRECIOUS! It's "+item)
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)
        elif type == "hit":
            self.strlist.append('Ohhh myyyy')
            self.strlist.append('Well met, traveller!')
            self.strlist.append('Oh, who do we have here? Fancy a cuppa?')
            self.strlist.append('That tickled!!')
            self.strlist.append("Oh no you didn't. ")
            self.strlist.append('How dare you attacking me, you little punk! Come here and taste the blood.')
            self.strlist.append('HAHAHAHAHAH.. oops I mean.. URGH that hurts! ')
            self.strlist.append('Yessss I like it. Keep attacking me. *hrrrrrrrr*')
            self.strlist.append('Can you be more gentle please. I mean I have feelings too. I hate this monster stereotype. *hmpf*')

            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)

    def strRoom(self,type,room):
        player = room.player
        if type == "opening":
            self.strlist.append("You blink once or twice as you enter the room, trying to adjust to the darkness surrounding you, failing miserably.\n A little light would be useful!")
            self.strlist.append("'Ahh this room looks just like my basement', you think while trying to ignore the foul smell of death.")
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)

    def modify(self,string,player):
        if player is not None:
            if player.condition == "normal":
                return string
            elif player.condition == "poisoned":
                return ""
        else:
            return string
