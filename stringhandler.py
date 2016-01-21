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

        elif type == "killed":
            self.strlist.append("You killed "+ name+"!")
            self.strlist.append('You beat' +name+ 'into oblivion.')
            self.strlist.append(name+ ' is dead!')
            string = random.choice(self.strlist)

        elif type == "loot":
            self.strlist.append("Oh look, it's "+item+"!")
            self.strlist.append('Someone seems to favour you... A new '+item+'!')
            self.strlist.append('uuuuh, look what you found! You better keep that little precious '+item+", 'cause you will never know when you need it. *blink*")
            self.strlist.append("MY PRECIOUS! It's "+item)
            string = random.choice(self.strlist)

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

        elif type == "flee":
            self.strlist.append(name+' laughs manically as you try to flee from it')
            self.strlist.append('"Your soul is mine!"')
            self.strlist.append("'Nope dude! You ain't going nowhere!'")
            self.strlist.append("'Where do you think you're going?!'")
            self.strlist.append('')
            string = random.choice(self.strlist)

        elif type == "fleeSuccess":
            self.strlist.append('You barely manage, stumbling through the darkness ')
            self.strlist.append('Close call, mate. Try not to die, will you?')
            self.strlist.append('To be, or not to be?')
            self.strlist.append('Can you please watch out. You almost died.')
            string = random.choice(self.strlist)

        elif type == "fleeFail":
            self.strlist.append('As you run through the darkness you fall and hit your head on something.')
            self.strlist.append('You are tumbling through the darkness, trusting your reflexes to keep yourself on track.\nBut, alas, you have been betraid! You stuble, and your head crashes into a rock.')
            # self.strlist.append('')
            # self.strlist.append('')
            self.strlist.append('Can you please watch out. You almost died.')
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strMonsterDamage(self,type,monster,damage,player):
        name = str(Fore.GREEN+" "+monster.getShortName()+" "+ Fore.WHITE)
        namelong = str(Fore.GREEN+" "+monster.getFullName()+" "+ Fore.WHITE)
        damage =str(Fore.RED+" "+str(damage)+" "+Fore.WHITE)
        hp = str(Fore.GREEN +" "+ str(monster.getHP()) +" "+ Fore.WHITE)

        if type == "getAttacked":
            self.strlist.append('Bam, right in the muzzle. That was' + damage + 'damage!')
            self.strlist.append('Boom. Right in his face! Keep going.' + damage + 'damage for the monster.')
            self.strlist.append('You attack ' +name+ ' and you deal' + damage + 'damage.')
            # self.strlist.append('')
            # self.strlist.append('')
            string = random.choice(self.strlist)


        elif type == "returnHP":
            self.strlist.append("The monster's health is now at"+hp )
            self.strlist.append('If it bleeds, you can kill it!')
            string = random.choice(self.strlist)


        elif type == "spawn":
            self.strlist.append('A wild'+ namelong + 'appears!'+ name + 'attacks you.')
            self.strlist.append("What's this?! Oh no it's"+ namelong+ "!")
            self.strlist.append('Crap, not another one of those... \nThis one looks like'+ namelong+ "!")
            self.strlist.append("'Why hello there! I am" + namelong +"\nPleased to meet you. NOT!'")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strRoom(self,type,room):
        player = room.player
        if type == "opening":
            self.strlist.append("You blink once or twice as you enter the room, trying to adjust to the darkness surrounding you, failing miserably.\nA little light would be useful!")
            self.strlist.append("'Ahh this room looks just like my basement', you think while trying to ignore the foul smell of death.")
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)


    def strPlayerDamage(self,type,player,monster,damage):
        damage =str(Fore.RED+" "+str(damage)+" "+Fore.WHITE)
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +" "+Fore.WHITE)
        monster = str(Fore.GREEN +monster.getShortName()+Fore.WHITE)

        if type == "takeDamage":
            self.strlist.append(monster+' hits you hard. You take'+damage+'damage!')
            # self.strlist.append('')
            string = random.choice(self.strlist)
        if type == "hp":
            self.strlist.append('Do you WANT to die?')
            self.strlist.append('Only'+ hp+ 'drops of blood left,'+playerName+'!')
            self.strlist.append("'Tis but a scratch!")
            self.strlist.append("It's only a fleshwound!"+hp+"life left.")
            self.strlist.append('Life is slowly slipping away... ')
            # self.strlist.append('')
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strPlayer(self,type,player):
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +""+Fore.WHITE)

        if type == "lvl":
            self.strlist.append('\nCongratulations "+playerName+", you leveled up!\n')
            self.strlist.append('\nDing.\n')
            self.strlist.append('\nDong.\n')
            self.strlist.append('\nNext Level! Here you go!\n')
            string = random.choice(self.strlist)
            del self.strlist[:]
            return self.modify(string,player)


    def modify(self,string,player):
        if player is not None:
            if player.condition == "normal":
                return string
                #return self.killString(string)
            elif player.condition == "poisoned":
                print "poisoned"
                return self.killString(string)
        else:
            return string
            # print "else"
            # return self.killString(string)

    def killString(self,string):
        newString = ""
    	builder = ""
    	for i in range(len(string)):
    		letter = string[i]
    		if((letter == " ") or (letter == ".") or (letter == ",")):
    			newString += builder[-1] + builder[1: -1] + builder[0] + " "
    			builder = ""
    		else:
    			builder += letter
    	return newString
